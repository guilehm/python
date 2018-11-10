import requests
from lxml.html import fromstring


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[5][contains(text(),"elite proxy")]') and i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ':'.join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return list(proxies)


if __name__ == '__main__':
    proxies = get_proxies()
