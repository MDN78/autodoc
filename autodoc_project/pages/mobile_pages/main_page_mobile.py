from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy

class AndroidMainPage:

    def authorization(self, login, password):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/autotvLogin')).send_keys(login)
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/password')).send_keys(password)
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/signInBtn')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Главная'))


    def search_product(self, name, number):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/action_search')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/search_src_text')).send_keys(f'{name} {number}')
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/btnSearch')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/text_section')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text(name))

    def add_item_to_cart(self, name, number):
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/action_search')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/search_src_text')).send_keys(f'{name} {number}')
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/btnSearch')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/text_section')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/priceItemPriceClOut')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/floatingButton')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/txtBottomMenuCart')).click()
        browser.element((AppiumBy.ID, 'ru.autodoc.autodocapp:id/cartItemManAndArt')).should(have.text(f'{name} {number}'))


android_main_page = AndroidMainPage()