from autodoc_project.api.board_api import board_api
import pytest


# @pytest.mark.skip
def test_add_item_to_cart():
    token = board_api.get_auth_token()
    board_api.add_item_to_cart("ZIC", "132661", token)
    board_api.clear_cart(token)
