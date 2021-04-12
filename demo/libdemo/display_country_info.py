import requests


def get_border_countries(countries : list[dict], country : dict) -> str:
    borders = country['borders']
    names = []
    for code in borders:
        country = get_country(countries, code)
        names.append(country['name'])

    return ",".join(names)


def get_languages(langs : list[dict]) -> str:
    names = [l['name'] for l in langs]
    return ",".join(names)


def get_country(countries: list[dict], code: str) -> dict:
    for c in countries:
        if c['alpha3Code'] == code:
            return c

    return None


response = requests.get(f"https://restcountries.eu/rest/v2/all")
countries = response.json()
code = input("Enter country code :")
country = get_country(countries, code)

if country is None:
    print("Sorry! Could not find country!")
    exit()

print("Name         : ", country['name'])
print("Capital      : ", country['capital'])
print("Population   : ", country['population'])
print("Area         : ", country['area'])
print("Borders      : ", get_border_countries(countries, country))
print("Languages    : ", get_languages(country['languages']))
