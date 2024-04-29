import allure
from allure_commons.types import Severity
from autodoc_project.api.board_api import board_api

@allure.feature('API')
@allure.tag('API')
@allure.story('Add item to cart')
@allure.title('Add item to cart via API')
@allure.severity(Severity.NORMAL)
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_add_item_to_cart():
    token = board_api.get_auth_token()
    board_api.add_item_to_cart("ZIC", "132661", token)
    board_api.clear_cart(token)
