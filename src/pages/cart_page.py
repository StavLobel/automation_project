from selenium.webdriver.common.by import By
from .base_page import BasePage
import re


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".cart_item")  # No items means cart is empty

    def load(self):
        self.driver.get(self.URL)

    def get_cart_items(self):
        return [item.text for item in self.driver.find_elements(*self.ITEM_NAMES)]

    def _data_test_value(self, prefix, item_name):
        # Only lowercase and replace spaces with hyphens, preserve all other characters
        return f"{prefix}{item_name.lower().replace(' ', '-')}"

    def remove_item_by_name(self, item_name):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        for item in items:
            if item.text == item_name:
                parent = item.find_element(By.XPATH, "../../..")
                data_test = self._data_test_value("remove-", item_name)
                try:
                    remove_btn = parent.find_element(
                        By.XPATH, f".//button[@data-test='{data_test}']"
                    )
                    remove_btn.click()
                    return True
                except Exception:
                    return False
        return False

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0
