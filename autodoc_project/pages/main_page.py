import allure
from selene import browser, have, be
from autodoc_project.data.users import User
from autodoc_project.data.cars import Car
from utils.logger import step


class MainPage:

    @step
    @allure.step("open browser")
    def open(self):
        browser.open("/")

    @step
    @allure.step('Authorization registered user')
    def authorization_registered_user(self, user: User):
        browser.element('#loginInfo').click()
        browser.element('#Login').should(be.blank).send_keys(user.username)
        browser.element('#Password').should(be.blank).send_keys(user.password)
        browser.element('.icon.fa').click()
        browser.element('#submit_logon_page').click()
        browser.element('#user_info').should(have.exact_text(user.username))

    @step
    @allure.step('Authorization unregistered user')
    def authorization_unregistered_user(self, user: User):
        browser.element('#loginInfo').click()
        browser.element('#Login').should(be.blank).send_keys(user.username)
        browser.element('#Password').should(be.blank).send_keys(user.password)
        browser.element('.icon.fa').click()
        browser.element('#submit_logon_page').click()
        browser.element('#errorMessage').should(have.exact_text('Неудалось авторизоваться.'))

    @step
    @allure.step("Checking authorization form")
    def registration_form_should_have_exact_visible_text(self):
        browser.element('.registration').click()
        browser.element('.title').should(have.text('Регистрация пользователя'))

    @step
    @allure.step("Search")
    def search_item_by_tool_number(self, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(value)
        browser.element('.search-button').click()
        browser.element('.breadcrumbs-header').should(have.text(value))

    @step
    @allure.step("Search by VIN number")
    def search_by_vin_number(self, car: Car):
        browser.element('[name=vin]').should(be.blank).send_keys(car.vin)
        browser.element('.btn-transparent').click()
        browser.element('.breadcrumbs').should(have.text('Оригинальный каталог'))

    @step
    @allure.step("Checking phrase")
    def main_page_should_have_visible_text(self):
        browser.element('.homepage-content__title').should(have.exact_text('Запчасти в интернет-магазине Автодок'))


main_page = MainPage()
