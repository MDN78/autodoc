import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.pages.ui_pages.main_page import main_page


@allure.tag('Autodoc')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'User')
@allure.feature('Authorization')
@allure.story('Auth registered user')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_authorization_registered_user():
    main_page.open()
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    main_page.authorization_registered_user(registered_user)


@allure.tag('Autodoc')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'User')
@allure.feature('Authorization')
@allure.story('Auth registered user')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_registered_user_should_be_authorized():
    main_page.open()
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    main_page.authorization_registered_user(registered_user)
    main_page.user_should_be_authorized(registered_user.username)


@allure.tag('Autodoc')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'User')
@allure.feature('Authorization')
@allure.story('Auth registered user')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_authorized_user_page():
    main_page.open()
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    main_page.authorization_registered_user(registered_user)
    main_page.main_page_auth_user_should_have_exact_visible_text('Баланс')
