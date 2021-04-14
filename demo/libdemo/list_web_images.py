import requests
from bs4 import BeautifulSoup


def extract_filename(path):
    if '/' in path:
        pos = path.rfind("/")
        return path[pos + 1:]
    else:
        return path


url = input("Enter website :")
try:
    response = requests.get(url)
    if response.status_code != 200:
        print("Sorry! Error accessing website!")
        exit()

    bs = BeautifulSoup(response.text, "html.parser")
    for img in bs.find_all("img"):
        if 'src' in img.attrs:
            print(extract_filename(img['src']))

except Exception as ex:
    print("Error : ", ex)
