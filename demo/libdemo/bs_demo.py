from bs4 import BeautifulSoup

markup = "<h2 style='color:red'>Topics</h2><ul><li>Requests</li><li>Beautiful Soup</li></ul>"
bs = BeautifulSoup(markup, "html.parser")
print(bs.h2.text)
print(bs.h2['style'])
print("Using find_all() attribute")
for li in bs.find_all("li"):
    print(li.text)

print("Using children attribute")
for li in bs.ul.children:
    print(li.text)