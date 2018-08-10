import bs4
import requests

res = requests.get("http://nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, "lxml")
type(no_starch_soup)
