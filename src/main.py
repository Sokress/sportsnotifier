import sys
import requests
import config

def fetchAPI():
    response = requests.get("https://basketapi1.p.rapidapi.com/api/basketball/search/kevin", headers={
        'X-RapidAPI-Key': config.api_key,
        'X-RapidAPI-Host': config.api_host
    })
    if response.status_code == 200:
        data = response.json()
        print(data)

    else:
        print("Error")
    return data


def main():
    app = fetchAPI()


if __name__ == "__main__":
    sys.exit(main())
