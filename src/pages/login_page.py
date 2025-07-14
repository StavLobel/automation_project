"""
Login page object for SauceDemo automation.
Handles login actions and error message retrieval.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the SauceDemo login page."""

    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        """Navigate to the login page."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Fill in credentials and submit the login form."""
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        """Return the error message text if present, else None."""
        if self.is_visible(*self.ERROR_MESSAGE):
            return self.find(*self.ERROR_MESSAGE).text
        return None
