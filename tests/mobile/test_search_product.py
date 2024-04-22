from autodoc_project.pages.mobile_pages.main_page_mobile import android_main_page

def test_search_product():
    android_main_page.authorization('SPA-49335', 'C602E21C')
    android_main_page.search_product('ZIC', '132661')