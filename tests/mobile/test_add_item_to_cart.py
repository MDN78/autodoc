from autodoc_project.pages.mobile_pages.main_page_mobile import android_main_page

def test_add_item_to_cart():
    android_main_page.authorization('SPA-49335', 'C602E21C')
    android_main_page.add_item_to_cart('ZIC', '132661')