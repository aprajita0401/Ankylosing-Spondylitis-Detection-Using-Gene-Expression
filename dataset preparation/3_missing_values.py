#3
#fill the missing values
import pandas as pd

df = pd.read_excel('AS.xlsx')

# Fill missing values only in numeric columns with column mean
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

df.to_excel('AS_cleaned.xlsx', index=False)
print("Missing values handled and cleaned data saved.")
