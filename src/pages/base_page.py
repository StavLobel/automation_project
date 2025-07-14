from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value):
        element = self.find(by, value)
        element.click()

    def type(self, by, value, text):
        element = self.find(by, value)
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, value):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except Exception:
            return False
