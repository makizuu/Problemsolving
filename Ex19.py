import requests
from bs4 import BeautifulSoup

base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser', multi_valued_attributes=None)
title = soup.find_all('p')

for text in title:
    if text.string != None and text.get('class') != 'content-header__row content-header__dek':
        print(text.string)