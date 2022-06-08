from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)

print(response.text)
