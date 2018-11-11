from collections import namedtuple

import requests
from bs4 import BeautifulSoup

URL = 'https://free-proxy-list.net/'

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
table_rows = soup.find('table', id='proxylisttable').tbody.find_all('tr')

Proxy = namedtuple('Proxy', ['ip', 'port', 'country', 'anonymity', 'https', 'last_checked'])
proxies = []

for tr in table_rows:
    tr_data = [td.text for td in tr]
    proxies.append(Proxy(tr_data[0], tr_data[1], tr_data[3], tr_data[4], tr_data[6], tr_data[7]))

print(proxies)
