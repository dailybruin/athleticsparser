from bs4 import BeautifulSoup
import urllib2
import json

url = "http://www.uclabruins.com//ViewContent.dbml?DB_OEM_ID=30500&CONTENT_ID=1409164"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

data = {}
data["categories"] = []

names = soup.find_all('table')
for name in names:
   names = name.find_all('h3')

   for name in range(len(names)):
   		data["categories"].append({"name": names[name].string, "categories": []})

sections = soup.find('center').find('font').find_all('font')
for center in range(len(sections)):
	if sections[center].find('h3'):
		center = sections[center].find('center').find('h3')
		print center


jsonData = json.dumps(data)

print jsonData