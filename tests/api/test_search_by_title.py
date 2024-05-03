import allure
from allure_commons.types import Severity
from autodoc_project.api.board_api import board_api
from utils.validator_json import validator_json_scheme


@allure.tag('API')
@allure.story('Search item by title and number')
@allure.title('Search item by title and number via API')
@allure.severity(Severity.NORMAL)
@allure.feature('API')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_search_by_title_and_number(base_api_url):
    resp = board_api.search_by_title_and_number('ZIC', '132661', base_api_url)
    validator_json_scheme(resp, 'search_scheme.json')
    assert resp[0] == 'ZIC'
    assert resp[1] == '132661'
    assert resp[3] == 200
