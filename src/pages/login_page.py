from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        if self.is_visible(*self.ERROR_MESSAGE):
            return self.find(*self.ERROR_MESSAGE).text
        return None
