"""
Base page object for all pages in the SauceDemo automation project.
Provides common Selenium utility methods for element interaction and waiting.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class for all page objects. Handles driver and common actions."""

    def __init__(self, driver, timeout=10):
        """
        Initialize the page object.
        :param driver: Selenium WebDriver instance
        :param timeout: Default wait timeout for element actions
        """
        self.driver = driver
        self.timeout = timeout

    def find(self, by, value):
        """Wait for and return a visible element by locator."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value):
        """Click an element by locator."""
        element = self.find(by, value)
        element.click()

    def type(self, by, value, text):
        """Type text into an input element by locator."""
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, value):
        """Check if an element is visible on the page."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except Exception:
            return False
