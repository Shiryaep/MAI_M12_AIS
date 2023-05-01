import urllib.request
import json
from geopy.geocoders import Nominatim

def getWeatherByCity(city):
    getStr = "http://wttr.in/" + city + "?format=\"" + "%l:%t\""
    contents = urllib.request.urlopen(getStr).read()
    return contents.decode('utf-8', 'ignore')

def getWeatherByCityV2(city):
    data = getWeatherJSON(city)
    returnValue = {"city": city, "unit":"celsius", "temperature":data['current_weather']['temperature']}
    return returnValue

def getWeatherJSON(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    webRequest = '''https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&current_weather=true&windspeed_unit=ms&forecast_days=7&timezone=Europe%2FMoscow'''.format(location.latitude, location.longitude)
    contents = urllib.request.urlopen(webRequest).read()
    my_json = contents.decode('utf-8').replace("'",'"')
    data = json.loads(my_json)
    return data


if (__name__ == "__main__"):

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode("New York")
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)

    webRequest = '''https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&current_weather=true&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FMoscow'''.format(location.latitude, location.longitude)
    contents = urllib.request.urlopen(webRequest).read()
    my_json = contents.decode('utf-8').replace("'",'"')
    print(my_json)
    print('- ' * 20)
    data = json.loads(my_json)
    print(data['hourly']['temperature_2m'][15])
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)