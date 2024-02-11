# Bonus Assignment 2: Webscraping

#In your second project, you will write a tool to extract and collect soccer data from [transfermark.com](https://www.transfermarkt.com/). This website provides data on soccer teams, and especially soccer players, from all relevant leagues around the globe.

#For this assignment, you should focus on extracting the available information for one league.

#Your program should have at least a minimal interface to interact with the data. You could for #example use the following options (depending on the focus of your program):
# 1. Show available teams
#  2. Select team and show high level information on the team
#  3. Select team and and show all players of the team
#  4. Stop the program

import requests
import bs4

userAgent = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

url = "https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1"

r = requests.get(url, headers=userAgent)
htmlText = r.text
htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")

table = htmlDocument.find('table', {'class': 'items'}).find('tbody')
teams = table.find_all('tr') 



def showTeams():
    print("\nShow available teams:")
    for i, team in enumerate(teams, 1):
        name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
        print(f"{i}: {name}")

def teamInfo(team_index):
    team = teams[team_index]
    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
    info = team.find_all("td", {"class": "zentriert"})
    squad = info[1].text
    age = info[2].text
    foreigners = info[3].text
    marketValue = team.find_all("td", {"class": "rechts"})
    averageMV = marketValue[0].text
    totalMV = marketValue[1].text.strip()
    print(f"\n{name} - Important Information:")
    print(f"Number of players in squad: {squad}")
    print(f"Average age: {age}")
    print(f"Foreigners in team: {foreigners}")
    print(f"Average market value: {averageMV}")
    print(f"Total market value: {totalMV}")

def showPlayers(team_index):
    team = teams[team_index]
    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
    link_to_team = team.find('td', {'class': 'hauptlink no-border-links'}).a.get('href')

    r = requests.get("https://www.transfermarkt.com" + link_to_team, headers=userAgent)
    htmlText = r.text
    teamHtmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")

    print(f"\nPlayers of team {name}:")
    playersTable = teamHtmlDocument.find('table',{'class': 'items'}).find('tbody')
    players = playersTable.find_all('td', {'class': 'hauptlink'})
    for player in players:
       if len(player["class"]) != 1:
           continue
       player_name = player.text.strip()
       print(player_name)

while True:
    print("\nMenu:")
    print("1. Show available teams")
    print("2. Select a team and show important information")
    print("3. Select a team and show all players")
    print("4. Exit the program")

    choice = input("Please choose an option: ")

    if choice == '1':
        showTeams()

    elif choice == '2':
        team_index = int(input("Enter the number of the team: ")) - 1
        teamInfo(team_index)

    elif choice == '3':
        team_index = int(input("Enter the number of the team: ")) - 1
        showPlayers(team_index)

    elif choice == '4':
        print("End of the program.")
        break
    else:
        print("Please choose an option between 1 and 4!")


