# Review Scripts

The following scripts are designed to facilitate the automated analysis of data exported from the Web of Science (WoS) database.

## Usage

The different scripts can be utilized according to specific analytical requirements.

```sh
python <file>.py
```

### File Concatenation

The script `concatenate_xlsx.py` merges multiple Excel spreadsheets into a single consolidated table. Please ensure that the input tables have an identical structure to enable accurate concatenation. This script is particularly useful for aggregating multiple XLSX files exported from WoS.

### Ordering

The script `ordering.py` allows for the sorting and filtering of records based on user-defined criteria, with the final output provided in XLSX format.

### Highlighting

The scripts `script_highlight.py` and `script_highlight_excel.py` are used to highlight specified keywords from an Excel file. The output is generated in different formats: DOCX for `script_highlight.py` and XLSX for `script_highlight_excel.py`.

### Full Article Analysis

The script `analyse_articles_doi.py` retrieves full-text articles from the web based on DOIs listed in an Excel file. It subsequently highlights relevant terms within the full text of these articles, similar to the functionality provided by the other highlighting scripts.

