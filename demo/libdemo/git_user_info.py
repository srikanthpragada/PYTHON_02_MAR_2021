import requests

# user = "srikanthpragada"
user = input("Enter username :")
response = requests.get(f"https://api.github.com/users/{user}")
if response.status_code != 200:
    print(f"Sorry! Could not get details for {user} from github!")
    exit()

details = response.json()  # Convert JSON to dict

for key, value in details.items():
    if value is not None and len(str(value).strip()) > 0:
        print(f"{key:20}  - {value}")
