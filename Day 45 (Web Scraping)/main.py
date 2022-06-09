import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")

titles_list = [title.get_text() for title in titles]

string = ""
for title in reversed(titles_list):
    string += title + "\n"

with open("movies.txt", "w") as file:
    file.write(string)
