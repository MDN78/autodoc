import os
from autodoc_project.data.users import User
from autodoc_project.pages.mobile_pages.main_page_mobile import android_main_page


def test_add_item_to_cart():
    registered_user = User(
        username=os.getenv('USER_LOGIN'),
        password=os.getenv('USER_PASSWORD')
    )
    android_main_page.authorization(registered_user.username, registered_user.password)
    android_main_page.add_item_to_cart('ZIC', '132661')
