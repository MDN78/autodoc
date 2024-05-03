import allure
from allure_commons.types import Severity
from autodoc_project.pages.ui_pages.main_page import main_page


@allure.tag('UI-API')
@allure.feature('UI-API')
@allure.story('Search item by auth user')
@allure.title('Search item by auth user via UI + API')
@allure.severity(Severity.NORMAL)
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_search_form_by_item_number():
    main_page.open()
    main_page.search_item_by_tool_name_and_number('ZIC', '132661')
    main_page.check_search_result('ZIC')
