import pandas as pd
import numpy as np

# Step 1: Create a Date Range for a Full Month
start_date = "2024-10-01"  # Start date (year-month-day)
end_date = "2024-10-31"    # End date
dates = pd.date_range(start=start_date, end=end_date)

# Step 2: Create a DataFrame with Every Hour of the Month
data = {'Date': [], 'Hour': [], 'Vehicle_Count': []}

for date in dates:
    for hour in range(24):  # 0-23 hours for each day
        # Step 3: Generate Realistic Vehicle Count Based on Time of Day
        if 6 <= hour <= 9 or 17 <= hour <= 20:  # Morning and Evening Peak Hours
            vehicle_count = np.random.randint(500, 1000)  # High traffic
        elif 10 <= hour <= 16:  # Midday Traffic
            vehicle_count = np.random.randint(200, 450)  # Moderate traffic
        else:  # Night Traffic
            vehicle_count = np.random.randint(75,180)  # Low traffic
        # Append data to the dictionary
        data['Date'].append(date.strftime('%Y-%m-%d'))  # Format as YYYY-MM-DD
        data['Hour'].append(hour)
        data['Vehicle_Count'].append(vehicle_count)

# Step 4: Create a DataFrame
traffic_df = pd.DataFrame(data)

# Step 5: Save to CSV
file_name = "traffic_data.csv"
traffic_df.to_csv(file_name, index=False)
print(f"Dataset created and saved as {file_name}")
