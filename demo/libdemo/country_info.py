import requests


def get_languages(langs):
    names = [l['name'] for l in langs]
    return ",".join(names)


code = "IND"
response = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")

if response.status_code != 200:
    print("Sorry! Could not get details of country!")
    exit()

details = response.json()
print("Name         : ", details['name'])
print("Capital      : ", details['capital'])
print("Population   : ", details['population'])
print("Area         : ", details['area'])
print("Borders      : ", ",".join(details['borders']))
print("Languages    : ", get_languages(details['languages']))
