import urllib.request

city = input()

#contents = urllib.request.urlopen("http://google.com").read()
getString = "http://wttr.in/"
getString += city + "?format="
getString += "\""
getStringCorrectFormat = getString + "%l:%t"
getString += "%l:+%C+%t+%p+%T"
getString += "\""
getStringCorrectFormat +=  "\""

#print(getString)

contents = urllib.request.urlopen(getString).read()
#print('6\xc2\xb0C')
print(contents.decode('utf-8', 'ignore'))

print("\nCORRECT FORMAT")
contents = urllib.request.urlopen(getStringCorrectFormat).read()
#print('6\xc2\xb0C')
print(contents.decode('utf-8', 'ignore'))