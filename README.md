# 🧹 Automated Data Cleaning Tool

## Project Overview
This Python script automates the cleaning of messy e-commerce sales data. It transforms raw, inconsistent CSV files into analysis-ready datasets using the **Pandas** library.

## Key Features
- **Deduplication:** automatically removes duplicate transaction records.
- **Data Standardization:** Converts inconsistent date formats (e.g., "Jan 4, 2025") into standard ISO format (`YYYY-MM-DD`).
- **Text Cleaning:** Fixes capitalization and removes trailing whitespace from customer names.
- **Numeric Parsing:** Uses Regex to strip currency symbols (`$`, `,`) to enable mathematical analysis on sales figures.

## How to Use
1. **Setup:** Ensure Python and Pandas are installed (`pip install pandas`).
2. **Generate Data:** Run `01_generate_messy_data.py` to create a sample raw dataset.
3. **Clean Data:** Run `02_data_cleaner.py`.
4. **Result:** A new file `cleaned_sales_data.csv` will be generated in the directory.