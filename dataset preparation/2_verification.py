#2
#verify if all the columns are same or not
import pandas as pd

as_data = pd.read_excel('AS.xlsx')
norm_data = pd.read_excel('normal.xlsx')

# Check gene/probe IDs match perfectly
assert all(as_data['ID'] == norm_data['ID']), "Gene IDs do not match between AS and normal datasets!"

# Check number of genes and patient columns
print(f"AS shape: {as_data.shape}")
print(f"Normal shape: {norm_data.shape}")

# Check for missing values
print("Missing values in AS dataset:", as_data.isnull().sum().sum())
print("Missing values in normal dataset:", norm_data.isnull().sum().sum())
