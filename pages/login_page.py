from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.login_route = '/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        curr_url = self.browser.current_url
        assert self.login_route in curr_url, f'Ссылка не совпадает {curr_url}'

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form.is_displayed(), f'Элемент {login_form} не отображается на странице'

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.is_displayed(), f'Элемент {register_form} не отображается на странице'
