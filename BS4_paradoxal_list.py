import requests
from bs4 import BeautifulSoup

r = requests.get("https://pt.wikipedia.org/wiki/Lista_de_paradoxos")
soup = BeautifulSoup(r.content, "html.parser")

div = soup.find("div", class_="mw-parser-output")
paradox_kinds = [paradox.text for paradox in soup.find_all(class_="mw-headline")]

for kind in paradox_kinds:
    print(kind)
