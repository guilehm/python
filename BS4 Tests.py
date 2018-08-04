import csv

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.clark.wa.gov/sheriff/jail-roster')

soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())

# soup.prettify()

tds = soup.find_all('td')

for i in tds:
    print(i.get_text())

links = soup.find_all('a')

link_list = []
for link in links:
    link_list.append(link.get('href'))

for link in links:
    print(link)

for link in links:
    names = link.contents[0]
    print(names)

f = csv.writer(open('files/jail-roster.csv', 'w'))
f.writerow(['Name', 'Link'])

for link in links:
    names = link.contents[0]
    full_link = link.get('href')

    f.writerow([names, full_link])


trs = soup.find_all('tr')
# for tr in trs:
#     for link in tr.find_all('a'):
#         fulllink = link.get('href')
#         print(fulllink)
