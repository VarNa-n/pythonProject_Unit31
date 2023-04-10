# -*- encoding=utf8 -*-

from pages.base import WebPage
from pages.elements import WebElement
from pages.setting import site


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = f"{site}/login"

        print(f"****** {url}")
        super().__init__(web_driver, url)

    # Email
    email = WebElement(id='email')

    # Пароль
    password = WebElement(id="pass")

    # Кнопка "Войти"
    btn_success = WebElement(css_selector='button[type="submit"]')
