from bs4 import BeautifulSoup

markup = "<h2>Topics</h2><ul><li>Requests</li><li>Beautiful Soup</li></ul>"
bs = BeautifulSoup(markup, "html.parser")
print(bs.h2.text)
for li in bs.find_all("li"):
    print(li.text)