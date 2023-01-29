import sys
import requests
import config
from datetime import datetime

NBATEAMS = []


def fetchAPI(api):
    response = requests.get(
        f"https://basketapi1.p.rapidapi.com/api/basketball/{api}", headers={
            'X-RapidAPI-Key': config.api_key,
            'X-RapidAPI-Host': config.api_host
        })
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error")
    return data


def saveTeams(data):
    for conference in data["standings"][:2]:
        for team in conference["rows"]:
            NBATEAMS.append(team)


def displayTeams():
    print("\n--------NBA Teams--------")
    for i, team in enumerate(NBATEAMS):
        print(f"{i + 1}. {team['team']['name']}")

def uservalidation():
    displayTeams()
    while True:
        try:
            userinput = int(input("\nWhats your favorite Team 1 - 30: "))
            if userinput > 30 or userinput < 1:
                print("Invalid input")
            else:
                print(f"Your favorite team is: {NBATEAMS[userinput - 1]['team']['name']}")
                return NBATEAMS[userinput - 1]
        except ValueError:
            print("Invalid input")


def displayNextGame(userTeamNextgame):
    print("\n--------Next Match Info--------")
    for games in userTeamNextgame["events"][:5]:
        print(f"{games['homeTeam']['name']} vs {games['awayTeam']['name']}")
        print(f"Date: {datetime.fromtimestamp(games['startTimestamp']).strftime('%Y-%m-%d')}")
        print(f"Time: {datetime.fromtimestamp(games['startTimestamp']).strftime('%H:%M')}\n")


def displayPreviousGame(userTeamPreviousgame):
    print("\n--------Previous Match Info--------")
    for games in userTeamPreviousgame["events"][:3]:
        print(f"{games['homeTeam']['name']} vs {games['awayTeam']['name']}")
        print(f"Date: {datetime.fromtimestamp(games['startTimestamp']).strftime('%Y-%m-%d')}")
        print(f"Time: {datetime.fromtimestamp(games['startTimestamp']).strftime('%H:%M')}\n")


def main():
    teamData = fetchAPI("tournament/132/season/45096/standings/total")
    saveTeams(teamData)
    userTeam = uservalidation()
    userTeamPreviousgame = fetchAPI(f"team/{userTeam['team']['id']}/matches/previous/0")
    userTeamNextgame = fetchAPI(f"team/{userTeam['team']['id']}/matches/next/0")
    displayPreviousGame(userTeamPreviousgame)
    displayNextGame(userTeamNextgame)



if __name__ == "__main__":
    sys.exit(main())
