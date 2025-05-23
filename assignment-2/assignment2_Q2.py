# Q2.  By any plotting method, Find the Cst_Cnt station count number that has maximum variation in  the Salnty parameter.   [10 marks]

import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel('assignment-2/CALCOFI_DataSET.xlsx')

# Check the actual column names
print("Available columns:", df.columns)

# Assuming the relevant columns are "Cst_Cnt" and "Salnty"
# You might need to adjust the column name if it's like "Cst_Cnt ID" or "Cst_Cnt Station"
if "Cst_Cnt" not in df.columns or "Salnty" not in df.columns:
    raise ValueError("Dataset must contain 'Cst_Cnt' and 'Salnty' columns.")

# Drop rows where Salnty is missing
df = df.dropna(subset=["Salnty"])

# Group by Cst_Cnt and calculate Salnty standard deviation (variation)
Salnty_variation = df.groupby("Cst_Cnt")["Salnty"].std()

# Find the Cst_Cnt with the max variation
max_var_Cst_Cnt = Salnty_variation.idxmax()
max_var_value = Salnty_variation.max()

print(f"Cst_Cnt with max Salnty variation: {max_var_Cst_Cnt} (std: {max_var_value:.2f})")

# Plotting
plt.figure(figsize=(12, 6))
Salnty_variation.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.axhline(max_var_value, color='red', linestyle='--', label=f'Max Variation: {max_var_Cst_Cnt}')
plt.title("Salnty Variation by Cst_Cnt")
plt.xlabel("Cst_Cnt")
plt.ylabel("Salnty Std Deviation")
plt.legend()
plt.tight_layout()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



