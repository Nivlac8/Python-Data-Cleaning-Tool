# 🐍 Python Data Automation Portfolio

This repository contains Python tools designed to automate common data analysis tasks. These projects demonstrate proficiency in **ETL (Extract, Transform, Load)** processes, **data cleaning**, and **file system automation** using the `pandas` and `os` libraries.

---

## 📂 Project 1: Automated Data Cleaning Tool
**File:** `02_data_cleaner.py`

### Project Overview
This tool automates the pre-processing of raw, messy e-commerce datasets. It transforms inconsistent CSV files into "client-ready" data for analysis, eliminating hours of manual Excel work.

### Key Features
- **Deduplication:** Identifies and removes duplicate transaction records.
- **Smart Date Parsing:** Handles mixed date formats (e.g., "Jan 4, 2025" vs. "01/02/2025") and standardizes them to ISO format.
- **Data Validation:** Removes invalid rows (e.g., missing Order IDs).
- **Numeric Cleaning:** Uses Regex to strip currency symbols (`$`, `,`) and convert text to numbers.
- **String Normalization:** Fixes capitalization and removes hidden whitespace from customer names.

### How to Run
1. Run `01_generate_messy_data.py` to create a sample raw dataset.
2. Run `02_data_cleaner.py`.
3. **Result:** A clean file named `cleaned_sales_data.csv` is generated.

---

## 📂 Project 2: Automated Report Merger
**File:** `04_file_merger.py`

### Project Overview
This tool eliminates the manual work of combining multiple monthly reports. It automatically scans a directory for relevant CSV files and merges them into a single Master Report for year-end analysis.

### Key Features
- **Smart File Detection:** Uses the `os` library to identify files based on naming patterns (e.g., starts with `sales_`).
- **Batch Processing:** Loops through all matching files and reads them into memory.
- **Automated Concatenation:** Stacks multiple datasets into one unified dataframe using `pd.concat()`.
- **Scalability:** Capable of merging hundreds of files in seconds without manual copying and pasting.

### How to Run
1. Run `03_generate_monthly_files.py` to create dummy monthly reports (Jan, Feb, Mar).
2. Run `04_file_merger.py`.
3. **Result:** A unified file named `MASTER_SALES_REPORT.csv` is generated.

---

### 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Libraries:** `pandas`, `os`, `re` (Regex)
