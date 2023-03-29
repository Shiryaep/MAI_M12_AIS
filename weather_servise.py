import urllib.request

#contents = urllib.request.urlopen("http://google.com").read()
getString = "http://wttr.in/Vancouver?format="
getString += "\""
getString += "%l:+%C+%t+%p+%T"
getString += "\""

print(getString)

contents = urllib.request.urlopen(getString).read()

#print('6\xc2\xb0C')
print(contents.decode('utf-8', 'ignore'))