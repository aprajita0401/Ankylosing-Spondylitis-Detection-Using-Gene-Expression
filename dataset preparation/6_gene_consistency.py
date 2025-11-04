#6
#checks if both the files contains the same gene sequence
import pandas as pd

# Load the two datasets
df1 = pd.read_excel('AS_final_cleaned.xlsx')
df2 = pd.read_excel('normal_final_cleaned.xlsx')

# Extract gene/probe ID lists (assuming 'ID' column holds gene IDs)
genes_1 = df1['ID'].tolist()
genes_2 = df2['ID'].tolist()

# Check if gene sets are identical (ignoring order)
set_equal = set(genes_1) == set(genes_2)
print(f"Same genes (ignoring order): {set_equal}")

# Check if order is the same
order_equal = genes_1 == genes_2
print(f"Same gene order: {order_equal}")

# If gene sets are identical but order differs, reorder df2 to match df1
if set_equal and not order_equal:
    df2_reordered = df2.set_index('ID').loc[genes_1].reset_index()
    print("Reordered second dataset genes to match the first dataset order.")
else:
    df2_reordered = df2

# Now df1 and df2_reordered have consistent genes and order
