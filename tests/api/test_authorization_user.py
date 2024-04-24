import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.api.board_api import board_api
from utils.validator_json import validator_all_json_scheme


@allure.tag('API')
@allure.story('Validate JSON scheme via API')
@allure.title('Validate JSON scheme')
@allure.severity(Severity.NORMAL)
@allure.feature('Validate')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_validate_main_page_json_schema():
    url = os.getenv('JSON_API_URL')
    validator_all_json_scheme('main_page_json_scheme.json', url)


@allure.tag('API')
@allure.story('Auth registered user via API')
@allure.title('Auth registered user')
@allure.severity(Severity.NORMAL)
@allure.feature('Auth')
def test_authorization_user():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    board_api.authorization_user(registered_user)
