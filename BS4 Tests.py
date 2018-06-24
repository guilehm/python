import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.clark.wa.gov/sheriff/jail-roster')

soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())

# soup.prettify()

tds = soup.find_all('td')

for i in tds:
    print(i.get_text())
