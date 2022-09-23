from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
webpage_data = response.text
soup = BeautifulSoup(webpage_data, "html.parser")

find_td = soup.select("td a")

articles = soup.find_all(name="a", class_="titlelink")
print(articles)
articles_text = []
articles_link = []

for article_tag in articles:
    text = article_tag.getText()
    articles_text.append(text)
    link = article_tag.get("href")
    articles_link.append(link)

art_id = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_id = art_id.index(max(art_id))
print(articles_text)
print(articles_link)
print(art_id)
print(max_id)
max_art = [articles_text[max_id], articles_link[max_id], art_id[max_id]]
print(max_art)