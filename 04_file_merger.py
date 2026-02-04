import pandas as pd
import os

def merge_sales_files():
    # 1. Create an empty list to hold the dataframes
    all_data_frames = []
    
    # 2. Loop through every file in the current folder
    files = [f for f in os.listdir() if f.startswith('sales_') and f.endswith('.csv')]
    
    print(f"Found {len(files)} files to merge: {files}")

    for file in files:
        # Read the file
        df = pd.read_csv(file)
        # Add it to our list
        all_data_frames.append(df)
        print(f"Processed {file}...")

    # 3. Concatenate (Glue) them all together
    master_df = pd.concat(all_data_frames, ignore_index=True)

    # 4. Save the Master File
    master_df.to_csv('MASTER_SALES_REPORT.csv', index=False)
    print("\n--- SUCCESS! Created 'MASTER_SALES_REPORT.csv' ---")
    print(master_df)

if __name__ == "__main__":
    merge_sales_files()