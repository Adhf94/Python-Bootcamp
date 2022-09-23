import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_text = response.text
soup = BeautifulSoup(web_text, "html.parser")
titles = soup.find_all(name="h3", class_="title")

print(titles)

movies_list = [title.getText() for title in titles]

movies_list = movies_list[::-1]
print(movies_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")


