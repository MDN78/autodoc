# import pytest
# from selene import browser
# from autodoc_project.api.board_api import board_api
#
#
# @pytest.fixture
# def auth_driver():
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.open('https://www.autodoc.ru')
#     token = board_api.get_auth_token()
#     browser.driver.add_cookie({'name': 'accessToken', 'value': token})
#     browser.open('https://www.autodoc.ru')
#
#     yield
#
#     browser.quit()
