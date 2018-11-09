from concurrent import futures
import requests
from bs4 import BeautifulSoup


# USE THIS CODE FOR YOUR OWN RISK
# YOU MAY LAUNCH A DENIAL-OF-SERVICE (DoS) ATTACK


def get_images_urls(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        base = 'https://www.drpepper.com.br/tirinhas/'
        urls = [img.attrs['src'] for img in images if img.attrs.get('src', '').startswith(base)]
        print(f'Found {len(urls)} images.')
        return urls
    else:
        print(f'Error [{r.status_code}]')
        return


MAX_WORKERS = 20
BASE_URL = 'https://blog.drpepper.com.br/page/{}'


def get_all_images_urls(start, stop):
    pages_urls = [BASE_URL.format(number) for number in range(start, stop + 1)]
    workers = min(MAX_WORKERS, stop - start + 1)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = [url for url_list in list(executor.map(get_images_urls, pages_urls)) for url in url_list]
    return res


if __name__ == '__main__':
    urls = get_all_images_urls(1, 5)
