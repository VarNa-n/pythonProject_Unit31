import pytest
from pages.auth_page import AuthPage
from pages.setting import valid_email, valid_password, site

def test_auth(web_browser):
    """ Authorization on the site """

    page = AuthPage(web_browser)

    # Вводим логин-пароль
    page.email = valid_email
    page.password = valid_password

    page.btn_success.click()

    assert page.get_current_url() == site + "/all_pets"

    page.screenshot(file_name='screenshot.png')
