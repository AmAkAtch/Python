from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movie_list = [movie_title.getText() for movie_title in soup.find_all(name="h3", class_="title")]
movie_list.reverse()

with open("day45_web_scrapping/movie_list.txt", "w", encoding="utf-8") as file:
    file.writelines(f"{movie}\n" for movie in movie_list)

