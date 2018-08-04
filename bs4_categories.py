from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://www.guiadecompra.com/categorias/')
soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())
h2s = soup.find_all('h2')
categories = [h2.text for h2 in h2s]

print(categories)

with open('files/categories.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['Categorias'])
    writer.writeheader()
    for category in categories:
        writer.writerow({'Categorias': category})
