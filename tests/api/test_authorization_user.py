import os
from utils.validator_json import validator_all_json_scheme
from autodoc_project.pages.ui_pages.main_page import main_page
from autodoc_project.api.board_api import board_api
from autodoc_project.data.users import User


# @pytest.mark.skip
def test_validate_main_page_json_schema():
    url = 'https://webapi.autodoc.ru/api/client/profile'
    validator_all_json_scheme('main_page_json_scheme.json', url)


# @pytest.mark.skip
def test_authorization_user():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    board_api.authorization_user(registered_user)

#
# # @pytest.mark.skip
# def test_user_should_be_authorized(auth_driver):
#     main_page.user_should_be_authorized('SPA-49335')
#
#
# # @pytest.mark.skip
# def test_authorized_user_page(auth_driver):
#     main_page.main_page_auth_user_should_have_exact_visible_text('Баланс')
