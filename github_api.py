import requests
from collections import namedtuple

url = 'https://api.github.com/users/{}/gists'


def get_gists_data(username):
    r = requests.get(url.format(username))
    return r.json()


def get_gists_names(username):
    gists = get_gists_data(username)
    names = [filename for gist in gists for filename in gist['files']]
    return names


def get_gists(username):
    data = get_gists_data(username)
    main_info = [key for key in data[0]]
    Gist = namedtuple('Gist', main_info)
    gists = [Gist(**data) for data in data]
    return gists
