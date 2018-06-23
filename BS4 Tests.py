import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.clark.wa.gov/sheriff/jail-roster')

soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())
