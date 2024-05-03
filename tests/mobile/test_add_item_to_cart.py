import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.pages.mobile_pages.main_page_mobile import android_main_page

@allure.feature('Mobile')
@allure.tag('MOBILE')
@allure.story('Add item to cart')
@allure.title('Add item to cart mobile app')
@allure.severity(Severity.NORMAL)
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_add_item_to_cart():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    android_main_page.authorization(registered_user.username, registered_user.password)
    android_main_page.add_item_to_cart('ZIC', '132661')
    android_main_page.item_should_be_added_to_cart('ZIC', '132661')
