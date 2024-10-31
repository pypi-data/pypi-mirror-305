import pandas as pd
import os
from tkinter import Tk, filedialog, simpledialog
from tqdm import tqdm
import xlsxwriter
import numpy as np


def main():

    # Disable Tkinter main interface
    Tk().withdraw()

    # Open file dialog to select the Excel file
    excel_file_path = filedialog.askopenfilename(
        title="Select Excel File", filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    # Check if a file has been selected
    if not excel_file_path:
        print("No file was selected.")
        exit()

    # Load the selected Excel file
    xls = pd.ExcelFile(excel_file_path)

    # Display available sheet names
    sheet_names = xls.sheet_names
    print("\nAvailable sheets in this Excel file:")
    for idx, sheet_name in enumerate(sheet_names):
        print(f"{idx + 1}. {sheet_name}")

    # Ask the user to select which sheet to use
    while True:
        try:
            choice = int(input("\nEnter the number of the sheet to use: ")) - 1
            if 0 <= choice < len(sheet_names):
                selected_sheet = sheet_names[choice]
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    # Load the selected sheet
    df = pd.read_excel(xls, sheet_name=selected_sheet)

    # Display the first few rows to verify the file has been loaded correctly
    print(f"\nLoading sheet: {selected_sheet}")
    print(df.head())

    # Ask the user to select which columns to inspect
    print("\nAvailable columns in the selected sheet:")
    for idx, col_name in enumerate(df.columns):
        print(f"{idx + 1}. {col_name}")

    selected_columns = []
    while True:
        try:
            col_choice = input(
                "\nEnter the numbers of the columns to inspect (comma-separated, or press Enter to finish): "
            )
            if not col_choice:
                break
            col_indices = [int(num.strip()) - 1 for num in col_choice.split(",")]
            for idx in col_indices:
                if 0 <= idx < len(df.columns):
                    selected_columns.append(df.columns[idx])
                else:
                    print(
                        f"Column index {idx + 1} is out of range. Please enter a valid number."
                    )
            if selected_columns:
                break
        except ValueError:
            print("Please enter valid numbers separated by commas.")

    print(f"\nSelected columns to inspect: {selected_columns}")

    # Ask the user to select which columns to keep in the output file
    selected_output_columns = []
    while True:
        try:
            output_col_choice = input(
                "\nEnter the numbers of the columns to keep in the output file (comma-separated, or press Enter to finish): "
            )
            if not output_col_choice:
                break
            output_col_indices = [
                int(num.strip()) - 1 for num in output_col_choice.split(",")
            ]
            for idx in output_col_indices:
                if 0 <= idx < len(df.columns):
                    selected_output_columns.append(df.columns[idx])
                else:
                    print(
                        f"Column index {idx + 1} is out of range. Please enter a valid number."
                    )
            if selected_output_columns:
                break
        except ValueError:
            print("Please enter valid numbers separated by commas.")

    print(f"\nSelected columns to keep in output: {selected_output_columns}")

    # Ask the user for categories and corresponding keywords to highlight
    highlight_categories = {}
    while True:
        category_name = simpledialog.askstring(
            "Input Category", "Enter a category name (or press Cancel to finish):"
        )
        if not category_name:
            break
        keywords_input = simpledialog.askstring(
            "Input Keywords",
            f"Enter keywords for category '{category_name}' (comma-separated):",
        )
        if keywords_input:
            highlight_categories[category_name] = [
                kw.strip() for kw in keywords_input.split(",")
            ]

    # Define a palette of text colors that are colorblind-friendly and not too light
    highlight_colors = [
        "#FFA500",  # Orange
        "#008000",  # Green
        "#FF0000",  # Red
        "#0000FF",  # Blue
        "#800080",  # Purple
        "#000000",  # Black
        "#8B4513",  # Brown
    ]

    # Assign colors automatically to categories
    category_colors = {}
    for i, category in enumerate(highlight_categories):
        category_colors[category] = highlight_colors[i % len(highlight_colors)]

    # Display summary before processing
    total_rows = len(df)
    # output_excel_path = os.path.join(
    #     os.path.dirname(excel_file_path), "highlighted_document_formatted.xlsx"
    # )
    # Specify the output document path
    output_excel_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        title="Save Excel file as",
        filetypes=[("Excel files", "*.xlsx")],
    )

    print(f"\nProcessing file: {excel_file_path}")
    print("\nCategories and keywords to highlight:")
    for category, keywords in highlight_categories.items():
        print(f"- {category}: {', '.join(keywords)}")
    print(f"\nTotal rows to process: {total_rows}")
    print(f"Output file will be saved as: {output_excel_path}\n")

    # Create a new Excel workbook with xlsxwriter
    workbook = xlsxwriter.Workbook(output_excel_path)
    worksheet = workbook.add_worksheet("Highlighted Articles")

    # Write header row for the selected output columns
    header_format = workbook.add_format({"bold": True})
    for col_num, column_title in enumerate(selected_output_columns):
        worksheet.write(0, col_num, column_title, header_format)

    # Iterate over each row in the DataFrame to extract data and apply formatting
    for index, row in tqdm(df.iterrows(), total=total_rows, desc="Processing rows"):
        for col_num, col_name in enumerate(selected_output_columns):
            cell_value = row[col_name]
            # Handle NaN values by replacing them with an empty string
            if pd.isna(cell_value):
                cell_value = ""

            # Process only selected columns to inspect
            if col_name in selected_columns and isinstance(cell_value, str):
                words = cell_value.split()
                rich_text_segments = []
                for word in words:
                    formatted = False
                    for category, keywords in highlight_categories.items():
                        if any(keyword.lower() in word.lower() for keyword in keywords):
                            # Apply formatting: bold, font size 14, and color
                            format = workbook.add_format(
                                {
                                    "bold": True,
                                    "font_size": 11,
                                    "font_color": category_colors[category],
                                }
                            )
                            rich_text_segments.append(format)
                            rich_text_segments.append(word + " ")
                            formatted = True
                            break
                    if not formatted:
                        rich_text_segments.append(word + " ")

                # Write the rich text to the cell if there are multiple segments
                if len(rich_text_segments) > 1:
                    worksheet.write_rich_string(index + 1, col_num, *rich_text_segments)
                else:
                    worksheet.write(index + 1, col_num, cell_value)
            else:
                # Write without formatting for other columns
                worksheet.write(index + 1, col_num, cell_value)

    # Close the workbook to save the changes
    workbook.close()

    # Print the final file path
    print(f"\nProcessing complete. File saved as: {output_excel_path}")


if __name__ == "__main__":
    main()
