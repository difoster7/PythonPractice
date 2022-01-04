# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

nyt = 'https://www.nytimes.com/'
nyt_data = requests.get(nyt)
nyt_html = nyt_data.text

soup = BeautifulSoup(nyt_html, 'html.parser')
titles = str(soup.find_all('h3'))
for ar in titles:
    print(ar+",")