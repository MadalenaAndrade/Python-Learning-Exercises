# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, station: str):
        self.__station = station
        self.__observations = []
    
    def add_observation(self, observation: str):
        self.__observations.append(observation)
    
    def latest_observation(self):
        last = ""
        if self.__observations != []:
            last = self.__observations[-1]
        return last
    
    def number_of_observations(self):
        return len(self.__observations)

    def __str__(self):
        return f"{self.__station}, {len(self.__observations)} observations"
    
if __name__=="__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)