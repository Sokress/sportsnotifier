# Sports Notifier

A Python script that allows you to select your favorite NBA team and displays the next 5 upcoming games.

## Requirements

- Python 3.x
- requests

## Usage

1. Clone the repository: `git clone https://github.com/Sokress/sportsnotifier.git`
2. Create a `config.py` file and add the following:

```config.py
api_key = "<your_api_key>"
api_host = "<your_api_host>"
```
3. Run `main.py`: `python main.py`
4. Select your favorite team from the list.
5. The next 5 upcoming games for your favorite team will be displayed.

## API
This script uses [RapidAPI](https://rapidapi.com/skysports/api/skysports-basketball-v3) for fetching NBA team and match data. You need to sign up and get an API key to use this script.
## Contributor
[Sokress](https://github.com/Sokress)

[SlyRix](https://github.com/SlyRix)


## License
This project is licensed under the MIT License.