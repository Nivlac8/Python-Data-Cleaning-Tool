import pandas as pd

# Creating a intentionally messy dataset
data = {
    'Order_ID': [101, 102, 102, 104, None], 
    'Customer': [' calvin ', 'JANE DOE', '  john smith', 'ALICE', 'bob'],
    'Date': ['2025-01-01', '01/02/2025', '2025.01.03', 'Jan 4, 2025', '2025-01-05'],
    'Sales': ['$1,200', '850', '900', '1100.50', 'MISSING']
}

df = pd.DataFrame(data)
df.to_csv('messy_sales_data.csv', index=False)
print("Step 4 Complete: 'messy_sales_data.csv' created in your folder!")