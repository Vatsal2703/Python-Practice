#Q3. By any plotting method, Find the Cruise station count number  that has the average Temperature in degrees Celsius parameter as maximum.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (change file path if needed)
df = pd.read_excel('assignment-2/CALCOFI_DataSET.xlsx')

# Rename columns if necessary for easier access
df.columns = df.columns.str.strip()  # remove leading/trailing spaces

# Replace with your actual column names if they differ
group_col = 'Cst_Cnt'  # adjust to your actual column name
temp_col = 'T_degC'       # adjust if needed

# Drop rows with missing values in relevant columns
df = df[[group_col,temp_col]].dropna()

# Group by cruise station and calculate average temperature
avg_temp_by_station = df.groupby(group_col)[temp_col].mean()

# Find the station with the max average temperature
max_station = avg_temp_by_station.idxmax()
max_avg_temp = avg_temp_by_station.max()

print(f'Cruise Station with max average temperature: {max_station} ({max_avg_temp:.2f} °C)')

# Plotting
plt.figure(figsize=(12, 6))
avg_temp_by_station.sort_values(ascending=False).plot(kind='bar', color='orange')
plt.axhline(max_avg_temp, color='red', linestyle='--', label=f'Max Avg Temp: {max_avg_temp:.2f} °C')
plt.title('Average Temperature (°C) by Cruise Station Count')
plt.xlabel('Cruise Station Count')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.tight_layout()
plt.show()
