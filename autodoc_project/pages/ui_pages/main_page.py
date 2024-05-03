import allure
from selene import browser, have, be
from autodoc_project.data.users import User
from autodoc_project.data.cars import Car
from utils.logger import step


class MainPage:

    @step
    @allure.step("UI: open browser")
    def open(self):
        browser.open("/")

    @step
    def authorization_registered_user(self, user: User):
        with allure.step('UI: Authorization registered user'):
            browser.element('#loginInfo').click()
            browser.element('#Login').should(be.blank).send_keys(user.username)
            browser.element('#Password').should(be.blank).send_keys(user.password)
            browser.element('.icon.fa').click()
            browser.element('#submit_logon_page').click()

    @step
    def check_authorization_user(self, user: User):
        browser.element('#user_info').should(have.exact_text(user.username))

    @step
    @allure.step('UI: Authorization unregistered user')
    def authorization_unregistered_user(self, user: User):
        browser.element('.cabinet.ng-star-inserted').click()
        browser.element('#Login').send_keys(user.username)
        browser.element('#Password').send_keys(user.password)
        browser.element('.icon.fa').click()
        browser.element('#submit_logon_page').click()

    @step
    @allure.step('UI: Check form unregistered user')
    def check_error_message(self):
        browser.element('#errorMessage').should(have.exact_text('Не удалось авторизоваться.'))

    @step
    @allure.step("UI: Checking authorization")
    def user_should_be_authorized(self, user):
        browser.element('#user_info').should(have.exact_text(user))

    @step
    @allure.step("UI: Go to authorization form")
    def registration_form(self):
        browser.element('.registration').click()

    @step
    @allure.step("UI: Checking authorization form")
    def registration_form_should_have_exact_visible_text(self, value):
        browser.element('.title').should(have.text(value))

    @step
    @allure.step("UI: Checking balance form")
    def main_page_auth_user_should_have_exact_visible_text(self, name):
        browser.element('.balance-main').should(have.text(name))

    @step
    @allure.step("UI: Search")
    def search_item_by_tool_number(self, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(value)
        browser.element('.search-button').click()

    @step
    @allure.step("UI: Checking search form")
    def check_search_form(self, value):
        browser.element('.breadcrumbs-header').should(have.text(value))

    @step
    @allure.step("UI-API: Search")
    def search_item_by_tool_name_and_number(self, name, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(name, value)
        browser.element('.search-button').click()
        browser.element('.sub-nav.promark.ng-star-inserted').should(have.text(name))

    @step
    @allure.step("UI: Search by VIN number")
    def search_by_vin_number(self, car: Car):
        browser.element('[name=vin]').should(be.blank).send_keys(car.vin)
        browser.element('.btn-transparent').click()

    @step
    @allure.step("UI: Check research form by VIN number")
    def check_vin_search_result(self, value):
        browser.element('.breadcrumbs').should(have.text(value))

    @step
    @allure.step("UI: Checking phrase")
    def main_page_should_have_visible_text(self, value):
        browser.element('.homepage-content__title').should(have.exact_text(value))

    @step
    @allure.step("UI: Clear cart")
    def clear_cart(self):
        browser.element('.a-icon.a-cart').click()
        browser.element('.button-red').click()
        browser.element('.p-element.button-red.p-button.p-component').click()


main_page = MainPage()
