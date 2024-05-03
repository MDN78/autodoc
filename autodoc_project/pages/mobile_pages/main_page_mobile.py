import allure
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


class AndroidMainPage:

    def authorization(self, login, password):
        with allure.step('Authorization user'):
            browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/autotvLogin')).send_keys(login)
            browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/password')).send_keys(password)
            browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/signInBtn')).click()

    @allure.step('Checking maim page text')
    def main_page_should_have_text(self, text):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text(text))

    @allure.step('Search product')
    def search_product(self, name, number):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/action_search')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/search_src_text')).send_keys(f'{name} {number}')
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/btnSearch')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/text_section')).click()

    @allure.step('Checking search result')
    def page_should_have_text(self, name):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text(name))

    @allure.step('Add item to cart')
    def add_item_to_cart(self, name, number):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/action_search')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/search_src_text')).send_keys(f'{name} {number}')
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/btnSearch')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/text_section')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/priceItemPriceClOut')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/floatingButton')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/txtBottomMenuCart')).click()

    @allure.step('Checking item in cart')
    def item_should_be_added_to_cart(self, name, number):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/cartItemManAndArt')).should(
            have.text(f'{name} {number}'))


android_main_page = AndroidMainPage()
