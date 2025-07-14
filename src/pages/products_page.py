from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def load(self):
        self.driver.get(self.URL)

    def add_item_by_name(self, item_name):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        for item in items:
            if item.text == item_name:
                parent = item.find_element(By.XPATH, "../../..")
                add_btn = parent.find_element(
                    By.XPATH, ".//button[contains(@id, 'add-to-cart')]"
                )
                add_btn.click()
                return True
        return False

    def remove_item_by_name(self, item_name):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        for item in items:
            if item.text == item_name:
                parent = item.find_element(By.XPATH, "../../..")
                remove_btn = parent.find_element(
                    By.XPATH, ".//button[contains(@id, 'remove')]"
                )
                remove_btn.click()
                return True
        return False

    def get_cart_count(self):
        if self.is_visible(*self.CART_BADGE):
            return int(self.find(*self.CART_BADGE).text)
        return 0

    def go_to_cart(self):
        self.click(*self.CART_LINK)
