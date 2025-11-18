import math

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

file_name = 'stations1.csv'
full_path = PATH + file_name

def get_station_date(filename: str) -> dict:
    '''
    Input: CSV files with bike data

    Output: Dictionary with each station and lat/long {station: (longitute,latitude)}
    '''
    
    bike_dict = {}
    
    with open(full_path,'r') as bike_file:
        
        #skip first row with CSV headers
        next(bike_file)

        for line in bike_file:
            elements = line.replace('\n','').split(';')
            #print(elements)
            bike_dict[elements[3]] = float(elements[0]),float(elements[1])
    
    return bike_dict

def distance(stations: dict, station1: str, station2: str) -> float:
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict) -> tuple:
    station1 = ''
    station2 = ''
    greatest = 0
    
    for key1 in stations.keys():
        for key2 in stations.keys():
            d = distance(stations, key1, key2) 
            if d > greatest:
                station1 = key1
                station2 = key2
                greatest = d

    return station1, station2, greatest
 
if __name__ == '__main__':
    bikes = get_station_date(full_path)

    name1 = 'Viiskulma'
    name2 = 'Kaivopuisto'
    num = distance(bikes,name1,name2)
    #print(f'Distance is: {num}')

    #greatest_distance(bikes)
    station1, station2, greatest = greatest_distance(bikes)

    print(station1, station2, greatest)