import requests
from bs4 import BeautifulSoup

base_url = "https://www.nytimes.com/"
r = requests.get(base_url)
r_html = r.text
titles = []
soup = BeautifulSoup(r_html, features="html.parser")

for i in soup.find_all("h2","css-1vvhd4r e1voiwgp0"):
    titles.append(i.text)

for title in titles:
    print(title)