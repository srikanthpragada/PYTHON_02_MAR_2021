# Display countries that use given currency
import requests

currency = input("Enter currency code :")
response = requests.get(f"https://restcountries.eu/rest/v2/currency/{currency}")
countries = response.json()

for c in countries:
    print(f"{c['name']}")
