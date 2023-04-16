from pages.auth_page import MainPage
from pages.setting import site

def test_pet_friends (web_browser):

    page = MainPage(web_browser)
    page.scroll_down()

    assert page.get_current_url() == site + "/all_pets"
    page.screenshot("screenshot_main.png")