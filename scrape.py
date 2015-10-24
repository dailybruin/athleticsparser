from bs4 import BeautifulSoup
import urllib2

url = "http://www.uclabruins.com//ViewContent.dbml?DB_OEM_ID=30500&CONTENT_ID=1409164"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

titles = soup.findAll('font', attrs={"align": "left"})
for title in titles:
   print title.string

