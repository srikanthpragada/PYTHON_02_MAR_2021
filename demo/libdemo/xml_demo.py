
contents = """
<products>
  <product>
    <name>Product1</name>
    <price>9000</price>
  </product>
   <product>
    <name>Product2</name>
    <price>19000</price>
  </product>
   <product>
    <name>Product3</name>
    <price>5000</price>
  </product>
</products>
"""

from bs4 import BeautifulSoup

bs = BeautifulSoup(contents,"lxml-xml")
for product in bs.find_all("product"):
    name = product.find("name").text
    price = int(product.find("price").text)
    print(f"{name:20} {price:10}")

