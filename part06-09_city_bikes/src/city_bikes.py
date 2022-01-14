import math

def read_file(filename: str):
    with open(filename) as file:
        lines = []
        for line in file:
            line = line.replace('\n', '')
            line = line.strip()
            if 'longitude' in line.lower():
                continue
            lines.append(line)
        return lines

def get_station_data(filename: str):
    stations_raw = read_file(filename)
    stations = {}
    for station in stations_raw:
        station_data = station.split(';')
        name = station_data[3]
        long = float(station_data[0])
        lat = float(station_data[1])
        stations[name] = (long, lat)
    return stations

def distance(stations: dict, station1: str, station2: str):
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance_from_one_station(stations: dict, stations_list: list, station: str):
    start_index = stations_list.index(station)+1
    compare_list = stations_list[start_index:]
    greatest_tuple = None
    greatest = 0
    for compare in compare_list:
        d = distance(stations, station, compare)
        if d > greatest:
            greatest_tuple = (station, compare, d)
            greatest = d
    return greatest_tuple

def greatest_distance(stations: dict):
    stations_list = []
    for key, value in stations.items():
        stations_list.append(key)

    greatest_tuple = None
    greatest = 0
    for index, station in enumerate(stations_list):
        if index < len(stations_list)-1:
            stations_distance = greatest_distance_from_one_station(stations, stations_list, station)
            station1, station2, distance = stations_distance
            if distance > greatest:
                greatest_tuple = stations_distance
                greatest = distance

    return greatest_tuple

'''
import math

 

def get_station_data(filename:str):

    stations = {}

    with open(filename) as file:

        for row in file:

            parts = row.split(";")

            if parts[0] == "Longitude":

                continue

            stations[parts[3]] = (float(parts[0]), float(parts[1]))

 

    return stations

 

def distance(stations: dict, station1: str, station2: str):

    longitude1, latitude1 = stations[station1]

    longitude2, latitude2 = stations[station2]

 

    # Note, that this

    # longitude2, latitude2 = stations[station2]

    # ...is equivalent to

    #

    # coordinates = stations[station2]

    # longitude2 = coordinates[0]

    # latitude2 = coordinates[0]

 

    x_as_km = (longitude1-longitude2) * 55.26

    y_as_km = (latitude1-latitude2) * 111.2

    return math.sqrt(x_as_km**2 + y_as_km**2)

 

def greatest_distance(stations: dict):

    longest = 0

    for start_station in stations:

        for end_station in stations:

            e = distance(stations, start_station, end_station)

            if e > longest:

                station1 = start_station

                station2 = end_station

                longest = e

 

    return station1, station2, longest
'''