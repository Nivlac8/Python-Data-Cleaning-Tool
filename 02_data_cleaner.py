import pandas as pd

def clean_my_data():
    # 1. Load the messy file
    df = pd.read_csv('messy_sales_data.csv')
    
    # 2. Drop rows where Order_ID is missing (Gets rid of Bob's bad row)
    df = df.dropna(subset=['Order_ID'])

    # 3. Fix names
    df['Customer'] = df['Customer'].str.strip().str.title()

    # 4. Standardize Dates (The FIX: adding format='mixed')
    # This tells Python to handle "Jan 4", "01/02", and "2025-01-01" all at once.
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')

    # 5. Clean Sales
    df['Sales'] = df['Sales'].replace('[\$,]', '', regex=True)
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    # 6. Save the clean version
    df.to_csv('cleaned_sales_data.csv', index=False)
    
    print("\n--- CLEANING COMPLETE ---")
    print(df)

if __name__ == "__main__":
    clean_my_data()
