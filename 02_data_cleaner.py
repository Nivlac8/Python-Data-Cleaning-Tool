import pandas as pd

def clean_my_data():
    # 1. Load the messy file
    df = pd.read_csv('messy_sales_data.csv')
    print("Original Data:\n", df)

    # 2. Remove duplicates (The Order_ID 102 appears twice)
    df = df.drop_duplicates()

    # 3. Fix names (Remove spaces and make them Title Case)
    df['Customer'] = df['Customer'].str.strip().str.title()

    # 4. Standardize Dates (Converts everything to YYYY-MM-DD)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 5. Clean Sales (Remove '$' and make it a number)
    df['Sales'] = df['Sales'].replace('[\$,]', '', regex=True)
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    # 6. Save the clean version
    df.to_csv('cleaned_sales_data.csv', index=False)
    print("\n--- CLEANING COMPLETE ---")
    print(df)

if __name__ == "__main__":
    clean_my_data()