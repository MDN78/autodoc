import requests
import os
from dotenv import load_dotenv

load_dotenv()


class BoardApi():

    def get_auth_token(self):
        payload = {
            'username': os.getenv('USER_LOGIN'),
            'password': os.getenv('USER_PASSWORD'),
            'grant_type': 'password'
        }
        headers = {
            'authorization': 'Bearer',
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = requests.post('https://auth.autodoc.ru/token', data=payload, headers=headers)
        my_token = response.json()['access_token']
        return my_token

board_api = BoardApi()