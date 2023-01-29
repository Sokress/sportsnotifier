import os, sys
import requests
import json

class fetchAPI:
    def __init__(self):
        response = requests.get("https://basketapi1.p.rapidapi.com/api/basketball/team", headers={
    'X-RapidAPI-Key': '1e47c908femsh5ff05db5860aa9bp10eb84jsn72ff5c92edd7',
    'X-RapidAPI-Host': 'basketapi1.p.rapidapi.com'
  })
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            print(data)

        else:
            print("Error")
def main():
    app = fetchAPI()


if __name__ == "__main__":
    sys.exit(main())