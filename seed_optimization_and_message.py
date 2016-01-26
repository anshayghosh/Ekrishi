from seed import*
import geocoder
import pyowm
import googlemaps

def main():
    seed_list = []
    seed_list.append(seed("Wheat"))
    seed_list.append(seed("Rice"))
    seed_list.append(seed("Cotton"))
    seed_list.append(seed("Jute"))
    seed_list.append(seed("Banana"))
    seed_list.append(seed("Apple"))
    print get_altitude()
    print get_temperature()
    print get_address()
    print get_latlng()

    find_most_optimized_crop(seed_list,get_temperature(),get_altitude())


def get_altitude():
    g = geocoder.ip('me')
    gmaps = googlemaps.Client(key='AIzaSyCZXHznz1W3hZSbWqHZXtj6T1euVxyBitk')
    altitudes=gmaps.elevation((g.latlng[0],g.latlng[1]))
    final_altitude = altitudes[0]['elevation']
    return final_altitude

def get_temperature():
    g = geocoder.ip('me')
    owm = pyowm.OWM('65a34e19f4ad83823846b8fd1a1813fd')
    location  = g.city+","+g.country
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    return temperature

def get_address():
    g = geocoder.ip('me')
    return g.address

def get_latlng():
    g = geocoder.ip('me')
    new= str(g.latlng[0])+ " "+ str(g.latlng[1])
    return new

def find_most_optimized_crop(seed_list,temperature,altitude):
    alt_difference = [0,0,0,0,0,0]
    i=0
    while i<6:
        if (seed_list[i].check_if_right_temp(temperature)==True):
            alt_difference[i] = seed_list[i].absolute_difference_between_altitudes(altitude)
        i=i+1

    i=0
    min_diff=100000
    min_index=0
    while i<6:
        if (alt_difference[i]!=0):
            if(alt_difference[i]<min_diff):
                min_diff = alt_difference[i]
                min_index=i
        i=i+1
    return (seed_list[min_index]).name



