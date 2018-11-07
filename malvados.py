import os

import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


def extrair_url_tira(pagina):
    for extensao in ('html', 'htm'):
        r = requests.get(f'http://www.malvados.com.br/index{pagina}.{extensao}', headers=headers)
        if r.status_code == 200:
            break
    else:
        raise Exception(f'Nao consegui acessar a pagina {pagina}')

    root = etree.HTML(r.text)
    for x in root.findall('.//img'):
        if x.attrib.get('src', '').startswith('tir'):
            yield x.attrib['src']
            break
    else:
        # vamos apelar para o BeautifulSoup
        soup = BeautifulSoup(r.text)
        for x in soup.findAll('img'):
            if x.attrs.get('src', '').startswith('tir'):
                yield x.attrs['src']
                break
        else:
            raise Exception(f"Caramba, nao achei mesmo a imagem pra tirinha {pagina}")



def realizar_download(pagina, img_url):
    filename = f"output/{pagina:>04} - {img_url}"
    if os.path.exists(filename):
        return

    r = requests.get(f'http://www.malvados.com.br/{img_url}', headers=headers)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"{pagina} done")


def processar(inicio, fim):
    for pg in range(inicio, fim + 1):
        for url in extrair_url_tira(pg):
            realizar_download(pg, url)

# Coded by Roger
