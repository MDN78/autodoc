import allure
from allure_commons.types import Severity
from autodoc_project.api.board_api import board_api
from utils.validator_json import validator_json_scheme

@allure.feature('API')
@allure.tag('API')
@allure.story('Add item to cart')
@allure.title('Add item to cart via API')
@allure.severity(Severity.NORMAL)
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_add_item_to_cart(base_api_url):
    token = board_api.get_auth_token()
    board_api.add_item_to_cart("ZIC", "132661", token, base_api_url)
    current_response = board_api.get_json_scheme(base_api_url)
    part_name = current_response['items'][0]['priceItem']['manufacturer']['name']
    part_number = current_response['items'][0]['priceItem']['partNumber']
    assert part_number == "132661"
    assert part_name == "ZIC"
    validator_json_scheme(current_response, 'cart_scheme.json')
    board_api.clear_cart(token, base_api_url)
