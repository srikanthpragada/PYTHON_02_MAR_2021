# Display top 10 countries by density
import requests

response = requests.get(f"https://restcountries.eu/rest/v2/all")
countries = filter(lambda c: c['area'] is not None, response.json())

for c in sorted(countries,
                key=lambda cinfo: cinfo['population'] // cinfo['area'],
                reverse=True)[:10]:
    area = c['area']
    population = c['population']
    print(f"{c['name']:30} {population:10} {area:10} {population // area:5.0f}")
