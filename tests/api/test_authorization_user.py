import time

import requests
import os
import pytest
from selene import browser
from utils.validator_json import validator_all_json_scheme
from autodoc_project.pages.main_page import main_page
from autodoc_project.api.board_api import board_api
from autodoc_project.data.users import User

url = 'https://webapi.autodoc.ru/api/client/profile'


@pytest.mark.skip
def test_validate_main_page_json_schema(auth_driver):
    validator_all_json_scheme('main_page_json_scheme.json', url)

@pytest.mark.skip
def test_authorization_user():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    board_api.authorization_user(registered_user)

@pytest.mark.skip
def test_user_should_be_authorized(auth_driver):
    main_page.user_should_be_authorized('SPA-49335')


@pytest.mark.skip
def test_authorized_user_page(auth_driver):
    main_page.main_page_auth_user_should_have_exact_visible_text('Баланс')



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
