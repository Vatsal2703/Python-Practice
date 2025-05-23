import pandas as pd
import os

file_path = "Diabetes\diabetes.xlsx"
diabetes = pd.read_excel(file_path)
# print(diabetes.head())

# diabetic_data = diabetes[diabetes.iloc[:-1] == 1]
# min_age = min(diabetic_data["Age"])
# max_age = max(diabetic_data["Age"])
# print(min_age, max_age)


print(diabetes.describe())
