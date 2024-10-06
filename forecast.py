import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('traffic_data.csv')

# Combine 'Date' and 'Hour' into a single datetime column
data['datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Hour'].astype(str) + ':00')

# Take user input for date and hour
input_date = input("Enter the date (YYYY-MM-DD): ")
input_hour = int(input("Enter the hour (0-23): "))

# Convert input date to datetime object
input_datetime = datetime.strptime(input_date, '%Y-%m-%d')

# Check if the entered date is in the future relative to today
today = datetime.now()
if input_datetime <= today:
    print("Error: The entered date should be a future date.")
else:
    # Calculate the past 5 days for analysis relative to the input date
    print(f"Analyzing past traffic data for the last 5 days from {input_date} at {input_hour}:00.")
    
    past_counts = []
    dates = []

    for i in range(1, 6):  # Check the last 5 days relative to the input date
        past_date = input_datetime - timedelta(days=i)
        
        # Print for debugging: past date and hour being checked
        print(f"Checking data for {past_date.date()} at hour {input_hour}")

        # Filter the data for the same hour of the past date
        past_data = data[(data['datetime'].dt.date == past_date.date()) & (data['Hour'] == input_hour)]

        # Print the filtered data for debugging
        print("Filtered past data:", past_data)

        if not past_data.empty:
            past_counts.append(past_data['Vehicle_Count'].values[0])  # Take the count for that hour
            dates.append(past_date.date())  # Store the corresponding date

    # If past data is found, use it to predict future traffic count
    if past_counts:
        average_count = np.mean(past_counts)
        print(f"Predicted Traffic Count for {input_datetime}: {int(average_count)} (Based on Historical Data)")

        # Plotting the historical data and the predicted count
        formatted_dates = [date.strftime('%Y-%m-%d') for date in dates]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, past_counts, marker='o', label='Historical Counts', color='blue')
        plt.axhline(y=average_count, color='red', linestyle='--', label=f'Predicted Count for {input_date} at {input_hour}:00')
        plt.xlabel('Dates')
        plt.ylabel('Vehicle Count')
        plt.title(f'Traffic Count Prediction for {input_date} at {input_hour}:00')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"No historical data found for {input_hour}:00 on the last 5 days relative to {input_date}.")
