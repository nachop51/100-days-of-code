from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
tags = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in tags:
    article_texts.append(article_tag.get_text())
    article_links.append(article_tag.get("href"))
article_upvotes = [int(score.get_text().split()[0])
                   for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
most_upvoted = article_upvotes.index(max(article_upvotes))
print(article_texts[most_upvoted])
print(article_links[most_upvoted])
