#7
#normalises the values so as to make sure model trains well
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_excel('AS_final_cleaned.xlsx')

# Select numeric gene expression columns (assuming annotation columns are excluded)
numeric_cols = df.select_dtypes(include=['number']).columns
X = df[numeric_cols]

# Initialize scaler
scaler = StandardScaler()

# Fit and transform the data (z-score normalization)
X_normalized = scaler.fit_transform(X)

# Create a new DataFrame with normalized data and original gene/sample indexing
df_normalized = pd.DataFrame(X_normalized, columns=numeric_cols)

# If you want to keep gene IDs etc., add them back
for col in df.columns.difference(numeric_cols):
    df_normalized[col] = df[col].values

# Save normalized data
df_normalized.to_excel('AS_final_cleaned_normalized.xlsx', index=False)

print("Dataset normalized and saved.")
