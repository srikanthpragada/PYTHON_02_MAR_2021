import requests
from bs4 import BeautifulSoup
from datetime import *

response = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(response.text, "html.parser")
table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
rows = table.find_all("tr")
today = datetime.today()
for row in rows[1:]:  # ignore first row as it contains headings
    cols = row.find_all("td")
    name = cols[0].text
    timings = cols[1].text
    stdate = f"{cols[2].text}-{today.year}"
    sd = datetime.strptime(stdate, '%d-%b-%Y')
    days = (sd - today).days
    print(f"{name:40} {timings:15} {stdate:15} {days:3}")
