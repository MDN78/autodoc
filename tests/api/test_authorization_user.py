import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.api.board_api import board_api
from utils.validator_json import validator_json_scheme


@allure.tag('API')
@allure.story('Auth registered user')
@allure.title('Auth registered user via API')
@allure.severity(Severity.NORMAL)
@allure.feature('API')
def test_authorization_user(base_api_url):
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    resp = board_api.authorization_user(registered_user, base_api_url)
    status_code = resp[1]
    login = resp[2]
    with allure.step('Status code=204'):
        assert status_code == 200
    with allure.step('Check request - response'):
        assert login == registered_user.username
    with allure.step('Schema is validate'):
        validator_json_scheme(resp[0], 'auth_scheme.json')
