import pandas as pd
import matplotlib.pyplot as plt

file_path = "traffic_data.csv"  # Change to your file path
df = pd.read_csv(file_path)

# Step 2: Function to filter data based on user input date
def filter_data_by_date(df, input_date):
    filtered_df = df[df['Date'] == input_date]
    return filtered_df

# Step 2: Filter Data Based on User Input Date
input_date = input('Enter date in yyyy-mm-dd format')
filtered_df = df[df['Date'] == input_date]

# Step 3: Create Bar Graph 1 - Traffic for Each Hour of the Given Day
plt.figure(figsize=(14, 5))  # Set the figure size

# Subplot 1: Hourly Traffic
plt.subplot(1, 2, 1)  # Create a subplot for hourly traffic
plt.bar(filtered_df['Hour'], filtered_df['Vehicle_Count'], color='skyblue')
plt.title(f'Hourly Traffic on {input_date}')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Vehicles')
plt.xticks(filtered_df['Hour'])  # Show only hours present in the dataset

# Step 4: Calculate Peak and Least Traffic Hour
peak_hour = filtered_df.loc[filtered_df['Vehicle_Count'].idxmax(), 'Hour']
peak_traffic = filtered_df['Vehicle_Count'].max()
least_hour = filtered_df.loc[filtered_df['Vehicle_Count'].idxmin(), 'Hour']
least_traffic = filtered_df['Vehicle_Count'].min()

# Step 5: Create Bar Graph 2 - Peak and Lowest Traffic
plt.subplot(1, 2, 2)  # Create a second subplot for peak and least traffic
plt.bar(['Peak Hour', 'Lowest Hour'], [peak_traffic, least_traffic], color=['orange', 'lightgreen'])
plt.title(f'Peak and Lowest Traffic Hours on {input_date}')
plt.ylabel('Number of Vehicles')
plt.text(0, peak_traffic, f'Hour: {peak_hour}', ha='center', va='bottom', fontsize=12)
plt.text(1, least_traffic, f'Hour: {least_hour}', ha='center', va='bottom', fontsize=12)

# Step 6: Show Plots
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
