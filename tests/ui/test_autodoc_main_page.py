import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.cars import Car
from autodoc_project.pages.ui_pages.main_page import main_page


class TestMainPage:

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Checking authorization form')
    @allure.title('Checking authorization form via UI')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_registration_form_should_have_exact_visible_text(self):
        main_page.open()
        main_page.registration_form()
        main_page.registration_form_should_have_exact_visible_text('Регистрация пользователя')

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Search item by title and number')
    @allure.title('Search item by title and number via UI')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_search_form_by_item_number(self):
        main_page.open()
        main_page.search_item_by_tool_number('ZIC 132661')
        main_page.check_search_form('ZIC 132661')

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Checking main page')
    @allure.title('Checking main page via UI')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_main_page_should_have_exact_visible_text(self):
        main_page.open()
        main_page.main_page_should_have_visible_text()

    @allure.tag('UI')
    @allure.feature('UI')
    @allure.story('Search item by WIN number')
    @allure.title('Search item by WIN number via UI')
    @allure.severity(Severity.NORMAL)
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_search_by_vin_number(self):
        main_page.open()
        current_car = Car(
            vin=os.getenv('VIN_NUMBER'),
            manufacturer='',
            model=''
        )
        main_page.search_by_vin_number(current_car)
