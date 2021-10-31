import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

div = soup.find_all('div', class_='TableBase-overflow')

trs = div[0].find_all('tr', class_="TableBase-bodyTr")
# print(trs)

counter = 0
for tr in trs:
   counter +=1
   if counter <=20:
       td = tr.find_all('td')
       #get the player name
       info = td[0].find_all('span', class_='CellPlayerName--long')
       player_info = info[0].text
       player_split = " ".join(player_info.split())
       player_space = player_split.split(' ')

       team = player_space[-1]
       position = player_space[-2]
       name = player_space[0]+ ' ' + player_space[1]

       print("Player Name: " + name)
       print("Player Position: " + position)
       print("Player Team: " + team)

       #get player points scored
       points_td = td[12].text.strip()
       print("Points scored: " + points_td)

