import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from tkinter import Tk, filedialog
from tqdm import tqdm


def main():

    # File selection with dialog
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select the Excel file", filetypes=[("Excel files", "*.xlsx")]
    )

    if not file_path:
        print("No file selected. Ending program.")
        exit()

    data = pd.read_excel(file_path, sheet_name=None)  # Load all sheets to choose from

    # Display available sheets and select the sheet
    print("Available sheets:")
    sheet_names = list(data.keys())
    for i, name in enumerate(sheet_names):
        print(f"{i}: {name}")
    sheet_index = int(input("Enter the number of the sheet to use: "))
    selected_sheet = sheet_names[sheet_index]
    df = pd.read_excel(file_path, sheet_name=selected_sheet)

    # Store the total number of documents in the initial dataset
    total_initial_documents = len(df)

    # Display available columns and select columns to analyze
    print("Available columns:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")

    abstract_column_indices = input(
        "Enter the column numbers containing abstracts, separated by commas: "
    )
    abstract_columns = [df.columns[int(i)] for i in abstract_column_indices.split(",")]

    df["Text"] = ""
    for column in abstract_columns:
        df["Text"] += " " + df[column].fillna("")

    # Select columns to include in the final file
    selected_columns = input(
        "Enter the column numbers to include in the final file, separated by commas: "
    )
    selected_columns = [df.columns[int(i)] for i in selected_columns.split(",")]

    # Exclude rows containing specific terms
    exclude_terms = input(
        "Enter terms to exclude, separated by commas (default: intra-host, intrahost, intracellular, intra-cellular): "
    )
    exclude = (
        exclude_terms.split(",")
        if exclude_terms
        else ["intra-host", "intrahost", "intracellular", "intra-cellular"]
    )

    excluded_terms_rows = pd.DataFrame()
    for e in exclude:
        rows_to_exclude = df[df["Text"].str.contains(e, case=False, na=False)]
        if not rows_to_exclude.empty:
            rows_to_exclude.insert(0, "Reason for Exclusion", f"Contains term: '{e}'")
            excluded_terms_rows = pd.concat([excluded_terms_rows, rows_to_exclude])
        df = df[~df["Text"].str.contains(e, case=False, na=False)]

    # Define categories and associated keywords, then assign weights
    keywords = {}
    weights = {}
    while True:
        category = input("Enter the category name (or press Enter to finish): ")
        if not category:
            break
        terms = input(
            f"Enter keywords for the category '{category}', separated by commas: "
        )
        keywords[category] = [term.strip() for term in terms.split(",")]
        while True:
            try:
                weight = float(
                    input(f"Enter the weight for the category '{category}': ")
                )
                weights[category] = weight
                break
            except ValueError:
                print("Please enter a numeric value for the weight.")

    # TF-IDF scores and cosine similarity
    def compute_scores(text_data, key_terms):
        tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)
        search_terms_tfidf = tfidf_vectorizer.transform([" ".join(key_terms)])
        cosine_scores = linear_kernel(search_terms_tfidf, tfidf_matrix).flatten()
        return cosine_scores

    category_scores = {
        category: compute_scores(df["Text"], keywords[category])
        for category in keywords
    }

    # Apply weights
    for category in category_scores:
        category_scores[category] *= weights[category]

    # Normalize scores
    normalized_scores = {
        category: scores / np.max(scores) if np.max(scores) != 0 else scores
        for category, scores in category_scores.items()
    }

    scores_df = pd.DataFrame(normalized_scores)
    scores_df["Total Score"] = scores_df.sum(axis=1)

    # Exclude rows with empty cells in specific columns
    print("Available columns to check for empty cells:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")
    columns_to_check_indices = input(
        "Enter the column numbers to check for empty cells, separated by commas: "
    )
    columns_to_check = [df.columns[int(i)] for i in columns_to_check_indices.split(",")]

    empty_cells_excluded_rows = df[df[columns_to_check].isnull().any(axis=1)]
    empty_cells_excluded_rows.insert(
        0,
        "Reason for Exclusion",
        empty_cells_excluded_rows.apply(
            lambda row: f"Empty cell in required column(s): {', '.join([col for col in columns_to_check if pd.isna(row[col])])}",
            axis=1,
        ),
    )

    # Remove rows with empty cells
    df = df[~df[columns_to_check].isnull().any(axis=1)]

    # Ask user if they want to exclude rows with a total score of 0
    exclude_zero_total = (
        input("Do you want to exclude rows with a total score of 0? (yes/no): ")
        .strip()
        .lower()
    )
    if exclude_zero_total == "yes":
        excluded_rows = df.join(scores_df[scores_df["Total Score"] == 0])[
            selected_columns + list(category_scores.keys()) + ["Total Score"]
        ]
        excluded_rows.insert(0, "Reason for Exclusion", "Total score is 0")
        scores_df = scores_df[scores_df["Total Score"] != 0]
    else:
        excluded_rows = pd.DataFrame()

    # Exclude categories with a score of 0, as requested by the user
    excluded_categories_rows = pd.DataFrame()
    categories_to_exclude = input(
        "Enter the names of categories for which you want to exclude rows with a score of 0, separated by commas: "
    ).split(",")
    for category in categories_to_exclude:
        category = category.strip()
        if category in weights:
            rows_to_exclude = scores_df[scores_df[category] == 0]
            excluded_rows_for_category = df.join(
                rows_to_exclude, lsuffix="_left", rsuffix="_right"
            )[selected_columns + list(category_scores.keys()) + ["Total Score"]]
            excluded_rows_for_category.insert(
                0, "Reason for Exclusion", f"Score of 0 for category '{category}'"
            )
            excluded_categories_rows = pd.concat(
                [excluded_categories_rows, excluded_rows_for_category]
            )
            scores_df = scores_df[scores_df[category] != 0]

    # Merge scores with the original data and sort
    final_ranked_data = df.join(
        scores_df, lsuffix="_left", rsuffix="_right"
    ).sort_values(by="Total Score", ascending=False)
    final_ranked_data.dropna(subset=["Total Score"], inplace=True)

    # Select columns for the final output
    final_csv = final_ranked_data[
        selected_columns + list(category_scores.keys()) + ["Total Score"]
    ]
    print(final_csv)

    # Save output to an Excel file
    output_file = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Save the Excel file as",
    )
    if output_file:
        total_rows = (
            len(final_csv)
            + len(excluded_rows)
            + len(excluded_categories_rows)
            + len(empty_cells_excluded_rows)
            + len(excluded_terms_rows)
        )
        with tqdm(total=total_rows, desc="Saving Excel file", unit=" rows") as pbar:
            with pd.ExcelWriter(output_file) as writer:
                final_csv.to_excel(writer, sheet_name="Results", index=False)
                pbar.update(len(final_csv))
                if not excluded_rows.empty:
                    excluded_rows.to_excel(
                        writer, sheet_name="Excluded (Total Score 0)", index=False
                    )
                    pbar.update(len(excluded_rows))
                if not excluded_categories_rows.empty:
                    excluded_categories_rows.to_excel(
                        writer, sheet_name="Excluded (Category Score 0)", index=False
                    )
                    pbar.update(len(excluded_categories_rows))
                if not empty_cells_excluded_rows.empty:
                    empty_cells_excluded_rows.to_excel(
                        writer, sheet_name="Excluded (Empty Cells)", index=False
                    )
                    pbar.update(len(empty_cells_excluded_rows))
                if not excluded_terms_rows.empty:
                    excluded_terms_rows.to_excel(
                        writer, sheet_name="Excluded (Terms)", index=False
                    )
                    pbar.update(len(excluded_terms_rows))

                # Summary sheet with document counts
                summary_data = {
                    "Sheet Name": [
                        "Results",
                        "Excluded (Total Score 0)",
                        "Excluded (Category Score 0)",
                        "Excluded (Empty Cells)",
                        "Excluded (Terms)",
                        "Total Documents Processed",
                    ],
                    "Number of Documents": [
                        len(final_csv),
                        len(excluded_rows),
                        len(excluded_categories_rows),
                        len(empty_cells_excluded_rows),
                        len(excluded_terms_rows),
                        total_initial_documents,
                    ],
                }
                summary_df = pd.DataFrame(summary_data)
                summary_df.to_excel(writer, sheet_name="Summary", index=False)

        print(f"The results have been saved in {output_file}")
    else:
        print("No output file selected. Ending program.")


if __name__ == "__main__":
    main()
