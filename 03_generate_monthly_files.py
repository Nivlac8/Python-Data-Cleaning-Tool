import pandas as pd
import os

# Create dummy data for 3 months
jan_data = {'Month': ['Jan', 'Jan'], 'Product': ['A', 'B'], 'Sales': [100, 200]}
feb_data = {'Month': ['Feb', 'Feb'], 'Product': ['A', 'C'], 'Sales': [150, 300]}
mar_data = {'Month': ['Mar', 'Mar'], 'Product': ['B', 'C'], 'Sales': [220, 310]}

# Save them as separate files
pd.DataFrame(jan_data).to_csv('sales_jan.csv', index=False)
pd.DataFrame(feb_data).to_csv('sales_feb.csv', index=False)
pd.DataFrame(mar_data).to_csv('sales_mar.csv', index=False)

print("Step 1 Complete: Created sales_jan.csv, sales_feb.csv, and sales_mar.csv")