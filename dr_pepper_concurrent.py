import os
import random
import time
from concurrent import futures

import requests
from bs4 import BeautifulSoup

from headers_and_referers import headers_referers, headers_useragents

# USE THIS CODE FOR YOUR OWN RISK
# YOU MAY LAUNCH A DENIAL-OF-SERVICE (DoS) ATTACK

image_count = 0


def get_header(user_agent, referer):
    headers = {'user-agent': user_agent, 'referer': referer}
    return headers


def get_images_urls(url):
    r = requests.get(
        url, headers=get_header(random.choice(headers_useragents), referer=random.choice(headers_referers))
    )
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        base = 'https://www.drpepper.com.br/tirinhas/'
        urls = [img.attrs['src'] for img in images if img.attrs.get('src', '').startswith(base)]
        print(f'Found {len(urls)} images.')
        return urls
    elif r.status_code == 403:
        print(f'Error [{r.status_code}]. Trying again.')
        return get_images_urls(url)
    else:
        print(f'Error [{r.status_code}]')
        return


MAX_WORKERS = 35
BASE_URL = 'https://blog.drpepper.com.br/page/{}'
BASE_NAME = 'dr-pepper/'


def get_all_images_urls(start, stop):
    pages_urls = [BASE_URL.format(number) for number in range(start, stop + 1)]
    workers = min(MAX_WORKERS, stop - start + 1)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = [url for url_list in list(executor.map(get_images_urls, pages_urls)) if isinstance(url_list, list) for url in url_list]
    return res


def download_image(url):
    filename = os.path.basename(url)
    if os.path.exists(BASE_NAME + filename):
        print('\tImage already exists')
        return
    r = requests.get(
        url, headers=get_header(random.choice(headers_useragents), referer=random.choice(headers_referers))
    )
    if r.status_code == 200:
        with open(f'dr-pepper/{filename}', 'wb') as f:
            f.write(r.content)
        global image_count
        image_count += 1
        print(f'\tImage {filename} saved.')
    elif r.status_code == 403:
        return download_image(url)
    else:
        print(f'[{r.status_code}] - Could not find image at {url}.')


def download_all_images(urls):
    workers = min(MAX_WORKERS, len(urls))
    with futures.ThreadPoolExecutor(workers)as executor:
        res = executor.map(download_image, urls)
    return res


if __name__ == '__main__':
    t0 = time.time()
    urls = get_all_images_urls(1, 479)
    images = download_all_images(urls)
    elapsed = time.time() - t0
    print(f'{image_count} images were saved in {elapsed:.2f} seconds with {MAX_WORKERS} workers.')
