import requests
from bs4 import BeautifulSoup
from lxml import etree

r = requests.get("https://pt.wikipedia.org/wiki/Lista_de_paradoxos")
soup = BeautifulSoup(r.content, "html.parser")

div = soup.find("div", class_="mw-parser-output")
paradox_kinds = [paradox.text for paradox in soup.find_all(class_="mw-headline")]

for kind in paradox_kinds:
    print(kind)

print("=" * 90)

root = etree.HTML(r.content)
for x in root.findall(".//span[@class='toctext']"):
    print(x.text)
