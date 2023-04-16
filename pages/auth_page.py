# -*- encoding=utf8 -*-


import  os, pickle
from pages.base import WebPage
from pages.elements import WebElement
from pages.setting import site


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or f"{site}/login"

        super().__init__(web_driver, url)

    # Email
    email = WebElement(id='email')

    # Пароль
    password = WebElement(id="pass")

    # Кнопка "Войти"
    btn_success = WebElement(css_selector='button[type="submit"]')

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or f"{site}"

        super().__init__(web_driver, url)

        with open('my_cookies.txt', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)
        web_driver.refresh()