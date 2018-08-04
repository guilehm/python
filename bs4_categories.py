import csv
from itertools import zip_longest

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.guiadecompra.com/categorias/')
soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())
h2s = soup.find_all('h2')
sbtcats = soup.find_all('a', {'class': 'sbtcat'})

categories = [{'Categorias': h2.text} for h2 in h2s]
sub_categories = [{'Sub Categorias': sbtcat.text} for sbtcat in sbtcats]

categories = [h2.text for h2 in h2s]
sub_categories = [sbtcat.text for sbtcat in sbtcats]

rows = zip_longest(*([categories, sub_categories]), fillvalue='')

with open('files/categories.csv', 'w') as csv_file:
    fieldnames = ['Categorias', 'Sub Categorias']
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()

    for cat, sub in rows:
        writer.writerow({'Categorias': cat, 'Sub Categorias': sub})
