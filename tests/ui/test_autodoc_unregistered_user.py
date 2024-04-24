import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.users import User
from autodoc_project.pages.ui_pages.main_page import main_page


@allure.tag("Autodoc")
@allure.severity(Severity.NORMAL)
@allure.label("MDN78", "User")
@allure.feature("Authorization")
@allure.story("Auth unregistered user")
@allure.link("https://www.autodoc.ru/", name="Autodoc.ru")
def test_authorization_unregistered_user():
    main_page.open()
    unregistered_user = User(
        username=os.getenv("UNREGISTERED_USER_LOGIN"),
        password=os.getenv("UNREGISTERED_USER_PASSWORD"),
    )
    main_page.authorization_unregistered_user(unregistered_user)
