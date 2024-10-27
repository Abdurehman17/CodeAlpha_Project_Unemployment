import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"D:\Code Alpha DS\Unemployment in India.csv")

# Clean column names
data.columns = data.columns.str.strip().str.lower()

# Convert 'date' to datetime
data['date'] = pd.to_datetime(data['date'])

# Check for unique column names
print(data.columns)

# Visualize unemployment rate over time for a specific region (e.g., Andhra Pradesh)
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='estimated unemployment rate (%)', data=data[data['region'] == 'Andhra Pradesh'])
plt.title('Unemployment Rate in Andhra Pradesh Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid()
plt.show()
