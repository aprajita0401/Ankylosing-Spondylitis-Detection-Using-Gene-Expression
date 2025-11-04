#8
#checks if all the values has been normalized
import pandas as pd

df = pd.read_excel('AS_final_cleaned_normalized.xlsx')

print(df.describe())  # Basic stats across columns

means = df.mean(numeric_only=True)
stds = df.std(numeric_only=True)

print("Mean values range:", means.min(), "to", means.max())
print("Std dev values range:", stds.min(), "to", stds.max())
