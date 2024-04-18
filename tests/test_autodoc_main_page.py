import os
import allure

from autodoc_project.data.cars import Car
from allure_commons.types import Severity
from autodoc_project.pages.main_page import main_page


class TestMainPage:

    @allure.tag('Autodoc')
    @allure.severity(Severity.NORMAL)
    @allure.label('MDN78', 'User')
    @allure.feature('Main page')
    @allure.story('Checking main page')
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_registration_form_should_have_exact_visible_text(self):
        main_page.open()
        main_page.registration_form_should_have_exact_visible_text()

    @allure.tag('Autodoc')
    @allure.severity(Severity.NORMAL)
    @allure.label('MDN78', 'User')
    @allure.feature('Main page')
    @allure.story('Checking main page')
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_search_form_by_item_number(self):
        main_page.open()
        main_page.search_item_by_tool_number('ZIC 132661')

    @allure.tag('Autodoc')
    @allure.severity(Severity.NORMAL)
    @allure.label('MDN78', 'User')
    @allure.feature('Main page')
    @allure.story('Checking main page')
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_main_page_should_have_exact_visible_text(self):
        main_page.open()
        main_page.main_page_should_have_visible_text()

    @allure.tag('Autodoc')
    @allure.severity(Severity.NORMAL)
    @allure.label('MDN78', 'User')
    @allure.feature('Main page')
    @allure.story('Checking main page')
    @allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
    def test_search_by_vin_number(self):
        main_page.open()
        current_car = Car(
            vin=os.getenv('VIN_NUMBER')
        )
        main_page.search_by_vin_number(current_car)
