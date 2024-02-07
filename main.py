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

url = f'https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1' 
r = requests.get(url, headers=userAgent) 
htmlText = r.text 
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
table = htmlDocument.find('table', {'class': 'items'}).find('tbody')
teams = table.find_all('tr')

team = teams[0]
name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
print(name)


""" 
while True: 
    print('1. Show available teams') 
    print('2. Select team and show high level information on the team') 
    print('3. Select team and and show all players of the team')
    print('4. Quit') 
    userInput = int(input())
    
    if userInput == 1: 
       
        else:
            print(f'Failed (Status Code: {r.status_code})')
        print('Available teams:')
        print(15*'-')
    elif userInput == 2: 
    elif userInput == 3:
        #fnewnfoqe
    elif userInput == 4: 
        break
    else: 
        print('Invalid input')
"""