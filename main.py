# Bonus Assignment 2: Webscraping

#In your second project, you will write a tool to extract and collect soccer data from [transfermark.com](https://www.transfermarkt.com/). This website provides data on soccer teams, and especially soccer players, from all relevant leagues around the globe.

#For this assignment, you should focus on extracting the available information for one league.

#Your program should have at least a minimal interface to interact with the data. You could for #example use the following options (depending on the focus of your program):
#  1. Show available teams
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

def display_teams():
    print("\nVerfügbare Mannschaften:")
    for i in range(len(teams)):
        team = teams[i]
        name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
        print(f"{i + 1}: {name}")

def team_info(team_index):
    team = teams[team_index]
    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
    info = team.find_all("td", {"class": "zentriert"})
    squad = info[1].text
    age = info[2].text
    foreigners = info[3].text
    marketValue = team.find_all("td", {"class": "rechts"})
    averageMV = marketValue[0].text
    totalMV = marketValue[1].text.strip()
    print(f"\n{name} - Wichtige Informationen:")
    print(f"Anzahl der Spieler im Kader: {squad}")
    print(f"Durchschnittsalter: {age}")
    print(f"Ausländer im Team: {foreigners}")
    print(f"Durchschnittlicher Marktwert: {averageMV}")
    print(f"Gesamtmarktwert: {totalMV}")

def display_team_players(team_index):
    team = teams[team_index]
    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
    print(f"\nSpieler der Mannschaft {name}:")
    # Hier könntest du den Code einfügen, um die Spieler der Mannschaft anzuzeigen

while True:
    print("\nMenü:")
    print("1. Verfügbare Mannschaften anzeigen")
    print("2. Eine Mannschaft auswählen und wichtige Informationen anzeigen")
    print("3. Mannschaft auswählen und alle Spieler anzeigen")
    print("4. Programm beenden")

    choice = input("Bitte wählen Sie eine Option: ")

    if choice == '1':
        display_teams()

    elif choice == '2':
        team_index = int(input("Geben Sie die Nummer der Mannschaft ein: ")) - 1
        team_info(team_index)

    elif choice == '3':
        team_index = int(input("Geben Sie die Nummer der Mannschaft ein: ")) - 1
        display_team_players(team_index)

    elif choice == '4':
        print("Das Programm wird beendet.")
        break

    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")
