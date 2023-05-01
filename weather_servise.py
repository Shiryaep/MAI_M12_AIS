import urllib.request
import json

def getWeatherByCity(city):
    getStr = "http://wttr.in/" + city + "?format=\"" + "%l:%t\""
    contents = urllib.request.urlopen(getStr).read()
    return contents.decode('utf-8', 'ignore')


if (__name__ == "__main__"):

    webRequest = '''https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&hourly=temperature_2m&current_weather=true&windspeed_unit=ms&forecast_days=1&timezone=Europe%2FMoscow'''
    contents = urllib.request.urlopen(webRequest).read()
    my_json = contents.decode('utf-8').replace("'",'"')
    print(my_json)
    print('- ' * 20)
    data = json.loads(my_json)
    print(data['hourly']['temperature_2m'][15])
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)