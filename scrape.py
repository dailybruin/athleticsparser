from bs4 import BeautifulSoup
import urllib2
import json

# Sports Parser
url = "https://www.teamrankings.com/college-football/team/ucla-bruins/stats"
#url = "https://www.teamrankings.com/ncaa-basketball/team/ucla-bruins/stats"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

data = {}
data["categories"] = []

# Find names of categories
names = soup.find("div", {"class": "module"}).find_all("h2")
for name in range(len(names)):
	data["categories"].append({"name": names[name].string, "offense": {}, "defense": {}})

# Find values for offense and defense
names = soup.find("div", {"class": "module"}).find_all("h2")
for name in range(len(names)):
	rows = soup.find("div", {"class": "module"}).find_all("tbody")[name].find_all("tr")
	for row in rows:
		data["categories"][name]["offense"][row.find_all("td")[0].string] = row.find_all("td")[1].get_text().split(" ")[0]
		data["categories"][name]["defense"][row.find_all("td")[2].string] = row.find_all("td")[3].get_text().split(" ")[0]

jsonData = json.dumps(data)
print jsonData






# url = "http://www.uclabruins.com//ViewContent.dbml?DB_OEM_ID=30500&CONTENT_ID=1409164"
# html = urllib2.urlopen(url).read()
# soup = BeautifulSoup(html, "html.parser")

# data = {}
# data["categories"] = []

# names = soup.find_all('table')
# for name in names:
#    names = name.find_all('h3')

#    for name in range(len(names)):
#    		data["categories"].append({"name": names[name].string, "categories": []})

# sections = soup.find('center').find('font').find_all('font')
# for center in range(len(sections)):
# 	if sections[center].find('h3'):
# 		center = sections[center].find('center').find('h3')
# 		print center


# jsonData = json.dumps(data)

# print jsonData