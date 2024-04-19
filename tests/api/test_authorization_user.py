import time

import requests
import pytest
from selene import browser
from utils.validator_json import validator_all_json_scheme
from autodoc_project.pages.main_page import main_page
from autodoc_project.api.board_api import board_api

url = 'https://webapi.autodoc.ru/api/client/profile'


@pytest.mark.skip
def test_validate_main_page_json_schema():
    validator_all_json_scheme('main_page_json_scheme.json', url)


@pytest.mark.skip
def test_open():
    main_page.main_page_auth_user_should_have_exact_visible_text()


def test_user_should_be_authorized():
    main_page.user_should_be_authorized('SPA-49335')

# @pytest.mark.skip
# def test_authorization():
#     # get auth token
#     payload = {
#         'username': 'SPA-18418',
#         'password': '1973731',
#         'grant_type': 'password'
#     }
#     headers = {
#         'authorization': 'Bearer',
#         'content-type': 'application/x-www-form-urlencoded',
#     }
#     response = requests.post('https://auth.autodoc.ru/token', data=payload, headers=headers)
#     my_token = response.json()['access_token']
#     print(response.text)
#     print(my_token)
#     param = {
#         'withUpdate': True
#     }
#     head = {
#         'authorization': f'Bearer {my_token}'
#     }
#     auth = requests.get(url=url, params=param, headers=head)
#     print(auth.text)

# @pytest.mark.skip
# def test_open_page():
#     browser.open('https://www.autodoc.ru')
#     payload = {
#         'username': 'SPA-18418',
#         'password': '1973731',
#         'grant_type': 'password'
#     }
#     headers = {
#         'authorization': 'Bearer',
#         'content-type': 'application/x-www-form-urlencoded',
#     }
#     response = requests.post('https://auth.autodoc.ru/token', data=payload, headers=headers)
#     my_token = response.json()['access_token']
#
#     browser.driver.add_cookie({'name': 'accessToken', 'value': my_token})
#     browser.open('https://www.autodoc.ru')
#     time.sleep(3)
