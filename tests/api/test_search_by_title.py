import allure
from allure_commons.types import Severity
from autodoc_project.api.board_api import board_api


@allure.tag('API')
@allure.story('Search item by title and number via API')
@allure.title('Search item by title and number')
@allure.severity(Severity.NORMAL)
@allure.feature('Search check')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_search_by_title_and_number():
    resp = board_api.search_by_title_and_number('ZIC', '132661')
    assert resp[0] == 'ZIC'
    assert resp[1] == '132661'
