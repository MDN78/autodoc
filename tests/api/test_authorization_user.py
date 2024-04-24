import os
from utils.validator_json import validator_all_json_scheme
from autodoc_project.api.board_api import board_api
from autodoc_project.data.users import User


def test_validate_main_page_json_schema():
    url = os.getenv('JSON_API_URL')
    validator_all_json_scheme('main_page_json_scheme.json', url)


def test_authorization_user():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    board_api.authorization_user(registered_user)
