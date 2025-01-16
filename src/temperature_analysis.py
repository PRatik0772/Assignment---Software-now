import os
import pandas as pd
import json

def calculate_average_temperature(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    all_data = []

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        all_data.append(data)
    
    combined_data = pd.concat(all_data)
    
    # Melt the data to long format for easier manipulation
    combined_data = combined_data.melt(id_vars=['STATION_NAME', 'STN_ID'], 
                                       value_vars=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                                       var_name='Month', value_name='Temperature')

    # Calculate the average temperature for each month
    monthly_avg = combined_data.groupby('Month')['Temperature'].mean()

    # Save the result in JSON format in the 'outputs' folder
    result = monthly_avg.to_dict()
    with open('outputs/average_temp.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

def find_station_with_largest_range(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    station_ranges = {}

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        data = data.melt(id_vars=['STATION_NAME', 'STN_ID'], 
                         value_vars=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                         var_name='Month', value_name='Temperature')

        for station in data['STATION_NAME'].unique():
            station_data = data[data['STATION_NAME'] == station]
            temp_range = station_data['Temperature'].max() - station_data['Temperature'].min()
            station_ranges[station] = max(station_ranges.get(station, 0), temp_range)
    
    max_range_station = [station for station, temp_range in station_ranges.items() if temp_range == max(station_ranges.values())]

    # Save the result in JSON format in the 'outputs' folder
    with open('outputs/largest_temp_range_station.json', 'w') as json_file:
        json.dump(max_range_station, json_file, indent=4)

def find_warmest_and_coolest_station(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    station_temps = {}

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        data = data.melt(id_vars=['STATION_NAME', 'STN_ID'], 
                         value_vars=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                         var_name='Month', value_name='Temperature')

        for station in data['STATION_NAME'].unique():
            station_data = data[data['STATION_NAME'] == station]
            avg_temp = station_data['Temperature'].mean()
            if station not in station_temps:
                station_temps[station] = []
            station_temps[station].append(avg_temp)
    
    station_avg = {station: sum(temps) / len(temps) for station, temps in station_temps.items()}
    max_temp = max(station_avg.values())
    min_temp = min(station_avg.values())

    warmest = [station for station, temp in station_avg.items() if temp == max_temp]
    coolest = [station for station, temp in station_avg.items() if temp == min_temp]

    # Save the result in JSON format in the 'outputs' folder
    result = {
        "Warmest Station(s)": warmest,
        "Coolest Station(s)": coolest
    }
    with open('outputs/warmest_and_coolest_station.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

# Example usage
if not os.path.exists('outputs'):
    os.makedirs('outputs')

calculate_average_temperature('temperatures')
find_station_with_largest_range('temperatures')
find_warmest_and_coolest_station('temperatures')

