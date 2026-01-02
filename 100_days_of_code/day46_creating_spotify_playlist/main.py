import requests
import datetime
from bs4 import BeautifulSoup


date_input = input("Enter the Year you would like to travel back to: ")

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0"
}

response = requests.get(f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{date_input}", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

songs_list = []

rows = soup.select("table.wikitable tbody tr")

for row in rows:
    cells = row.select("td")
    if len(cells)>=2:
        song_name = cells[1].getText()
        song_name=song_name.strip('"')
        songs_list.append(song_name)

print(songs_list)