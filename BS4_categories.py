import csv
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.guiadecompra.com/categorias/")
soup = BeautifulSoup(r.content, "html.parser")

div = soup.find('div', class_='baseB')

categories = defaultdict(list)
category = None

for child in div.children:
    if child.name == 'h2':
        category = child.text
        continue

    categories[category].append(child.li.a.text)

with open("files/categories_2.csv", "w") as csv_file:
    fieldnames = ["categories", "sub categories"]
    writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=fieldnames)
    writer.writeheader()

    for cat, subs in categories.items():
        for sub in subs:
            writer.writerow({"categories": cat, "sub categories": sub})
