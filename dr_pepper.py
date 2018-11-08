import os
import requests
from bs4 import BeautifulSoup


def get_images(page):
    url = f'https://blog.drpepper.com.br/page/{page}'
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        base = 'https://www.drpepper.com.br/tirinhas/'
        urls = [img.attrs['src'] for img in images if img.attrs.get('src', '').startswith(base)]
        print(f'Found {len(urls)} images at page {page}.')
        return urls
    else:
        print('Could not request URL {url}')


def download_images(urls):
    for url in urls:
        filename = os.path.basename(url)
        if os.path.exists('dr-pepper/' + filename):
            print('\tImage already exists')
            continue
        r = requests.get(url)
        if r.status_code == 200:
            with open(f'dr-pepper/{filename}', 'wb') as f:
                f.write(r.content)
            print(f'\tImage {filename} saved.')
        else:
            print(f'Could not find image at {url}')


def process(start, stop):
    for page in range(start, stop + 1):
        urls = get_images(page)
        download_images(urls)
