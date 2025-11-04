#1
#remove unwanted columns and make sure the output has the same columns
import pandas as pd

# Load Excel files
as1 = pd.read_excel('AS1.xlsx')
as2 = pd.read_excel('AS2.xlsx')
normal1 = pd.read_excel('normal_1.xlsx')
normal2 = pd.read_excel('normal_2.xlsx')

# Extract gene ID sets
genes_as1 = set(as1['ID'])
genes_as2 = set(as2['ID'])
genes_norm1 = set(normal1['ID'])
genes_norm2 = set(normal2['ID'])

# Find common genes across all files
common_genes = genes_as1 & genes_as2 & genes_norm1 & genes_norm2

# Filter to keep only common genes
as1_filtered = as1[as1['ID'].isin(common_genes)].copy()
as2_filtered = as2[as2['ID'].isin(common_genes)].copy()
normal1_filtered = normal1[normal1['ID'].isin(common_genes)].copy()
normal2_filtered = normal2[normal2['ID'].isin(common_genes)].copy()

# Sort by gene ID for consistent ordering
as1_filtered.sort_values('ID', inplace=True)
as2_filtered.sort_values('ID', inplace=True)
normal1_filtered.sort_values('ID', inplace=True)
normal2_filtered.sort_values('ID', inplace=True)

# Merge AS datasets column-wise
as_merged = pd.concat([as1_filtered.reset_index(drop=True), as2_filtered.drop(as2_filtered.columns[:10], axis=1).reset_index(drop=True)], axis=1)

# Merge normal datasets column-wise
normal_merged = pd.concat([normal1_filtered.reset_index(drop=True), normal2_filtered.drop(normal2_filtered.columns[:10], axis=1).reset_index(drop=True)], axis=1)

# Save to new Excel files
as_merged.to_excel('AS.xlsx', index=False)
normal_merged.to_excel('normal.xlsx', index=False)

print("Filtered AS and normal datasets saved as AS.xlsx and normal.xlsx")
