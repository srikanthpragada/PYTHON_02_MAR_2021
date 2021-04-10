# Display top 10 countries by population
import requests

response = requests.get(f"https://restcountries.eu/rest/v2/all")
countries = response.json()

for c in sorted(countries,
                key=lambda cinfo: cinfo['population'],
                reverse=True)[:10]:
    area = c['area']
    population = c['population']
    print(f"{c['name']:30} {population:10} {area:10} {population // area:5.0f}")
