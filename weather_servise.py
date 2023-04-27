import urllib.request

def getWeatherByCity(city):
    getStr = "http://wttr.in/" + city + "?format=\"" + "%l:%t\""
    contents = urllib.request.urlopen(getStr).read()
    return contents.decode('utf-8', 'ignore')


if (__name__ == "__main__"):
    city = input()

    #contents = urllib.request.urlopen("http://google.com").read()
    getString = "http://wttr.in/" + city + "?format=\""
    getStringCorrectFormat = getString + "%l:%t\""
    getString += "%l:+%C+%t+%p+%T\""

    #print(getString)

    contents = urllib.request.urlopen(getString).read()
    #print('6\xc2\xb0C')
    print(contents.decode('utf-8', 'ignore'))

    print("\nCORRECT FORMAT")
    contents = urllib.request.urlopen(getStringCorrectFormat).read()
    #print('6\xc2\xb0C')
    print(contents.decode('utf-8', 'ignore'))
