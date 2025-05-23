import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('assignment-2\CALCOFI_DataSET.xlsx')

# Check for required columns
required_columns = ['Sta_ID', 'T_degC']
if not set(required_columns).issubset(df.columns):
    raise ValueError(f"Missing required columns: {required_columns}")

# Drop rows where temperature or Sta_ID is missing
df = df[['Sta_ID', 'T_degC']].dropna()

# Group by station and calculate average temperature
avg_temp_by_station = df.groupby('Sta_ID')['T_degC'].mean()

# Find station with max average temperature
max_station = avg_temp_by_station.idxmax()
max_temp = avg_temp_by_station.max()

print(f"Cruise Station with max average temperature: {max_station} ({max_temp:.2f} °C)")

# Plot
plt.figure(figsize=(12, 6))
avg_temp_by_station.plot(kind='bar', color='skyblue')
plt.bar(max_station, max_temp, color='red', label=f'Max Avg Temp: {max_station}')
plt.title('Average Temperature by Cruise Station')
plt.xlabel('Station ID')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
