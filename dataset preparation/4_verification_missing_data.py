#4
# check if all the missing spaces has been filled 
import pandas as pd

df_cleaned = pd.read_excel('normal_cleaned.xlsx')

missing_count = df_cleaned.isnull().sum().sum()

if missing_count == 0:
    print("No missing values remain, data is clean!")
else:
    print(f"There are still {missing_count} missing values in the dataset.")
