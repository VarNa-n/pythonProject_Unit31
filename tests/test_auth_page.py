import pickle

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

    # Save cookies of the browser after the login
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(web_browser.get_cookies(), cookies)

    page.screenshot(file_name='screenshot_pass.png')
