import csv
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

r = requests.get("https://pt.wikipedia.org/wiki/Lista_de_paradoxos")
soup = BeautifulSoup(r.content, "html.parser")

paradox_kinds = [paradox.text for paradox in soup.find_all(class_="mw-headline")]
