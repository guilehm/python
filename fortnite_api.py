import os

import requests

# https://documenter.getpostman.com/view/4499368/RWEjoGqD#92831331-3bae-4798-917c-6f0541fdb489

FORTNITE_API_KEY = os.environ.get('FORTNITE_API_KEY')


class UserAPI:
    def __init__(self, username):
        self.username = username
        self._platforms = None
        self._uid = None
        self.seasons = None
        self._headers = {'Authorization': FORTNITE_API_KEY}

    def get_user_id(self):
        url = 'https://fortnite-public-api.theapinetwork.com/prod09/users/id'
        data = {'username': self.username}
        response = requests.post(url=url, headers=self._headers, data=data).json()
        self._platforms = response['platforms']
        self._uid = response['uid']
        self.seasons = response['seasons']
        return response

    def get_user_stats(self):
        url = 'https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats'
        data = {
            'user_id': self._uid,
            'platform': self._platforms[0],  # TODO: Fix me
            'window': 'alltime',
        }
        response = requests.post(url=url, headers=self._headers, data=data).json()
        return response


class ItemsAPI:
    def __init__(self):
        self._headers = {'Authorization': FORTNITE_API_KEY}
        self._url = 'https://fortnite-public-api.theapinetwork.com/prod09/store/get'

    def get_items(self):
        data = {'language': 'en'}
        response = requests.post(url=self._url, data=data)
        return response.json()


class NewsAPI:
    def __init__(self):
        self._headers = {'Authorization': FORTNITE_API_KEY}
        self._url = 'https://fortnite-public-api.theapinetwork.com/prod09/stw_motd/get'

    def get_news(self):
        data = {'language': 'en'}
        response = requests.post(url=self._url, data=data)
        return response.json()


class ChallengesAPI:
    def __init__(self):
        self._headers = {'Authorization': FORTNITE_API_KEY}
        self._url = 'https://fortnite-public-api.theapinetwork.com/prod09/challenges/get'

    def get_challenges(self, season='current'):
        data = {'language': 'en', 'season': season}
        response = requests.post(url=self._url, data=data)
        return response.json()


class TopTenAPI:
    def __init__(self):
        self._headers = {'Authorization': FORTNITE_API_KEY}
        self._url = 'https://fortnite-public-api.theapinetwork.com/prod09/leaderboards/get'

    def get_top_ten(self, window='top_10_kills'):
        data = {
            'language': 'en',
            'window': window,
        }
        response = requests.post(url=self._url, data=data)
        return response.json()


class PatchnotesAPI:
    def __init__(self):
        self._headers = {'Authorization': FORTNITE_API_KEY}
        self._url = 'https://fortnite-public-api.theapinetwork.com/prod09/patchnotes/get'

    def get_patchnotes(self):
        response = requests.post(url=self._url)
        return response.json()
