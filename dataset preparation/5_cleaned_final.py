#5
# fills any missed spaces that has been left during missing_values.py
import pandas as pd

# Load cleaned data
df_cleaned = pd.read_excel('normal_cleaned.xlsx')

# Fill missing numeric columns with mean
numeric_cols = df_cleaned.select_dtypes(include=['number']).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].mean())

# Fill missing non-numeric columns with 'Unknown'
non_numeric_cols = df_cleaned.select_dtypes(exclude=['number']).columns
df_cleaned[non_numeric_cols] = df_cleaned[non_numeric_cols].fillna('Unknown')

# Check remaining missing values
missing_count = df_cleaned.isnull().sum().sum()
print(f'Missing values left after filling: {missing_count}')

# Save the fully filled dataset
df_cleaned.to_excel('normal_final_cleaned.xlsx', index=False)
print("All missing values handled and saved to AS_final_cleaned.xlsx")
