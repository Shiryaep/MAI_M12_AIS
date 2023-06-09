import urllib.request
import json
import os
from geopy.geocoders import Nominatim
import redis


def getForecastByCity(city, dt):
    data = getWeatherJSON(city)
    num = -1
    for i in range(len(data['hourly']['time'])):
        if data['hourly']['time'][i] == dt:
            num = i
    if num < 0:
        return "There is no weather for this date"
    returnValue = {"city": city, "unit": "celsius",
                   "temperature": data['hourly']['temperature_2m'][num]}
    return returnValue


def getWeatherByCityV2(city):
    data = getWeatherJSON(city)
    returnValue = {"city": city, "unit": "celsius",
                   "temperature": data['current_weather']['temperature']}
    return returnValue


def getWeatherJSON(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    webRequest = f'''{os.getenv("URL")}?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&current_weather=true&windspeed_unit=ms&forecast_days=7&timezone=Europe%2FMoscow'''
    contents = urllib.request.urlopen(webRequest).read()
    my_json = contents.decode('utf-8').replace("'", '"')
    data = json.loads(my_json)
    return data


if (__name__ == "__main__"):

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode("New York")
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)

    webRequest = f'''{os.getenv("URL")}?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&current_weather=true&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FMoscow'''
    contents = urllib.request.urlopen(webRequest).read()
    my_json = contents.decode('utf-8').replace("'", '"')
    print(my_json)
    print('- ' * 20)
    data = json.loads(my_json)
    print(data['hourly']['temperature_2m'][15])
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)