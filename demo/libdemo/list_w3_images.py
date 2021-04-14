import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.w3schools.com")
bs = BeautifulSoup(response.text, "html.parser")

for img in bs.find_all("img"):
    print(img['src'])
