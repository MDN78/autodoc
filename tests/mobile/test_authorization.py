import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.pages.mobile_pages.main_page_mobile import android_main_page

@allure.feature('Mobile')
@allure.tag('MOBILE')
@allure.story('Authorization')
@allure.title('Authorization registered user mobile app')
@allure.severity(Severity.NORMAL)
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_authorization():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    android_main_page.authorization(registered_user.username, registered_user.password)
