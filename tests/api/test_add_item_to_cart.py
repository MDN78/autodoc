from autodoc_project.api.board_api import board_api
from autodoc_project.pages.main_page import main_page


def test_add_item_to_cart():
    token = board_api.get_auth_token()
    board_api.add_item_to_cart("ZIC", "132661", token)
    board_api.clear_cart(token)



# def test_clear(auth_driver):
#     main_page.clear_cart()
