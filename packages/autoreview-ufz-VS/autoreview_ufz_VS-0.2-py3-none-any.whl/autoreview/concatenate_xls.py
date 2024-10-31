import pandas as pd
import os
from tkinter import Tk, filedialog
from pathlib import Path
from tqdm import tqdm


def main():

    # Disable Tkinter main interface
    Tk().withdraw()

    # Open file dialog to select the folder containing Excel files
    dossier = filedialog.askdirectory(title="Select Folder Containing Excel Files")

    # Check if a folder has been selected
    if dossier:
        # List all Excel files in the folder
        fichiers_excel = [
            f for f in os.listdir(dossier) if f.endswith(".xls") or f.endswith(".xlsx")
        ]

        if not fichiers_excel:
            print("No Excel files found in the selected folder.")
        else:
            print("Excel files found:", fichiers_excel)

            # List to store DataFrames
            dataframes = []

            # Load each Excel file and add it to the list with progress bar
            for fichier in tqdm(fichiers_excel, desc="Loading Excel files"):
                chemin_complet = os.path.join(dossier, fichier)
                df = pd.read_excel(chemin_complet)
                dataframes.append(df)

            # Merge all DataFrames into one with progress bar
            print("\nMerging DataFrames...")
            df_final = pd.concat(
                tqdm(dataframes, desc="Merging DataFrames"), ignore_index=True
            )

            # Ask the user where to save the merged Excel file
            save_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx")],
                title="Save Merged Excel File As",
            )

            # Save the merged DataFrame to a new Excel file
            if save_path:
                df_final.to_excel(save_path, index=False)
                print("Merging complete! File saved as:", save_path)
            else:
                print("Save operation cancelled.")
    else:
        print("No folder was selected.")


if __name__ == "__main__":
    main()
