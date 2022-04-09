from urllib.request import urlopen

html = urlopen('http://pythonscrapping.com/pages/html')
print(html.read())
