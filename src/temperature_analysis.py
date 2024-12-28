import os
import pandas as pd

def calculate_average_temperature(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    all_data = []

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        all_data.append(data)
    
    combined_data = pd.concat(all_data)
    combined_data['Month'] = pd.to_datetime(combined_data['Date']).dt.month

    monthly_avg = combined_data.groupby('Month')['Temperature'].mean()
    monthly_avg.to_csv('average_temp.txt', header=['Average Temperature'])

def find_station_with_largest_range(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    station_ranges = {}

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        for station in data['Station'].unique():
            station_data = data[data['Station'] == station]
            temp_range = station_data['Temperature'].max() - station_data['Temperature'].min()
            station_ranges[station] = max(station_ranges.get(station, 0), temp_range)
    
    max_range_station = [station for station, temp_range in station_ranges.items() if temp_range == max(station_ranges.values())]
    with open('largest_temp_range_station.txt', 'w') as file:
        file.write("\n".join(max_range_station))

def find_warmest_and_coolest_station(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    station_temps = {}

    for file in files:
        data = pd.read_csv(os.path.join(folder, file))
        for station in data['Station'].unique():
            station_data = data[data['Station'] == station]
            avg_temp = station_data['Temperature'].mean()
            if station not in station_temps:
                station_temps[station] = []
            station_temps[station].append(avg_temp)
    
    station_avg = {station: sum(temps) / len(temps) for station, temps in station_temps.items()}
    max_temp = max(station_avg.values())
    min_temp = min(station_avg.values())

    warmest = [station for station, temp in station_avg.items() if temp == max_temp]
    coolest = [station for station, temp in station_avg.items() if temp == min_temp]

    with open('warmest_and_coolest_station.txt', 'w') as file:
        file.write("Warmest Station(s):\n" + "\n".join(warmest))
        file.write("\nCoolest Station(s):\n" + "\n".join(coolest))

# Example usage
calculate_average_temperature('temperatures')
find_station_with_largest_range('temperatures')
find_warmest_and_coolest_station('temperatures')
