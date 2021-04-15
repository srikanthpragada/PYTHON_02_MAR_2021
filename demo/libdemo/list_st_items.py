import requests
from bs4 import BeautifulSoup
from datetime import *

# response = requests.get("http://www.srikanthtechnologies.com/rss.xml")
response = requests.get("http://www.binaryintellect.net/articles/rssfeed.aspx")
rss = response.text
# print(rss)
bs = BeautifulSoup(rss[3:], "lxml-xml")
today = datetime.today()
for item in bs.find_all("item"):
    title = item.find("title").text.strip()
    pubdate = item.find("pubDate").text
    pd = datetime.strptime(pubdate[:11], "%d %b %Y")
    days = (today - pd).days
    print(title)
    print(pubdate)
    print(f"{days} days old")
    print('-' * 50)
