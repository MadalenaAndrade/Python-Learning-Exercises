# tee ratkaisu tänne
# Write your solution here

def get_station_data(filename: str):

    stations = {}
    names = []
    longitudes = []
    latitudes =[]
    with open(filename) as file:
        parts_list = []
        for line in file:
            parts = line.split(";")
            if parts[0] != "Longitude":
                names.append(parts[3].strip())
                longitudes.append(float(parts[0].strip()))
                latitudes.append(float(parts[1].strip()))

    for i in range(len(names)):
        stations[names[i]] = (longitudes[i], latitudes[i])

    return stations

def distance(stations: dict, station1: str, station2: str):
    import math
    
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    
    x_km = (longitude1-longitude2)*55.26
    y_km = (latitude1-latitude2)*111.2
    distance_km = math.sqrt(x_km**2+y_km**2)
    
    return distance_km

def greatest_distance(stations: dict):
    
    greatest_distance = 0
    
    for station1, coordinates in stations.items():
        for station2, coordinates in stations.items():
            distance_km = distance(stations, station1, station2)
            if distance_km > greatest_distance:
                greatest_distance = distance_km
                stations_and_distance = (station1, station2, greatest_distance)
                
    return stations_and_distance




if __name__=="__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)