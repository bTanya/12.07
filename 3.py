from urllib.request import urlopen


r = urlopen('http://python.org',data=b'a=1&b=2')
print(r.read())