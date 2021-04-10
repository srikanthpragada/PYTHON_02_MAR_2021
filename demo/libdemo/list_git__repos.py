import requests

user = "srikanthpragada"
response = requests.get(f"https://api.github.com/users/{user}/repos")
if response.status_code != 200:
    print(f"Sorry! Could not get details for {user} from github!")
    exit()

repos = response.json()  # Convert JSON to dict

for repo in repos:
   print(repo['name'])
   print(repo['description'])
   print('-' * 50)