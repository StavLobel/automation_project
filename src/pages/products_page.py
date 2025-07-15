"""
Products page object for SauceDemo automation.
Handles adding/removing items to/from the cart and cart navigation.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import re
import logging


class ProductsPage(BasePage):
    """Page object for the SauceDemo products (inventory) page."""

    URL = "https://www.saucedemo.com/inventory.html"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def load(self):
        """Navigate to the products page."""
        self.driver.get(self.URL)

    def _data_test_value(self, prefix, item_name):
        """Generate the data-test attribute value for add/remove buttons."""
        return f"{prefix}{item_name.lower().replace(' ', '-')}"

    def add_item_by_name(self, item_name):
        """Add an item to the cart by its name. Returns True if successful."""
        from selenium.webdriver.support.ui import WebDriverWait
        import selenium.common.exceptions

        logger = logging.getLogger(__name__)
        items = self.driver.find_elements(*self.ITEM_NAMES)
        for item in items:
            if item.text == item_name:
                parent = item.find_element(By.XPATH, "../../..")
                data_test = self._data_test_value("add-to-cart-", item_name)
                logger.info(
                    f"[add_item_by_name] Looking for button with data-test='{data_test}' for item '{item_name}'"
                )
                try:
                    add_btn = parent.find_element(
                        By.XPATH, f".//button[@data-test='{data_test}']"
                    )
                    prev_count = self.get_cart_count()
                    add_btn.click()
                    logger.info(
                        f"[add_item_by_name] Clicked add button for '{item_name}'"
                    )
                    try:
                        WebDriverWait(self.driver, 5).until(
                            lambda d: self.get_cart_count() == prev_count + 1
                        )
                        logger.info(
                            f"[add_item_by_name] Cart count updated to {self.get_cart_count()} after add."
                        )
                        return True
                    except selenium.common.exceptions.TimeoutException:
                        logger.warning(
                            f"[add_item_by_name] Cart count did not update after adding '{item_name}'."
                        )
                        return False
                except Exception as e:
                    logger.warning(
                        f"[add_item_by_name] Could not find/click add button for '{item_name}': {e}"
                    )
                    return False
        logger.warning(f"[add_item_by_name] Item '{item_name}' not found on page")
        return False

    def remove_item_by_name(self, item_name):
        """Remove an item from the cart by its name. Returns True if successful."""
        from selenium.webdriver.support.ui import WebDriverWait
        import selenium.common.exceptions

        logger = logging.getLogger(__name__)
        items = self.driver.find_elements(*self.ITEM_NAMES)
        for item in items:
            if item.text == item_name:
                parent = item.find_element(By.XPATH, "../../..")
                data_test = self._data_test_value("remove-", item_name)
                logger.info(
                    f"[remove_item_by_name] Looking for button with data-test='{data_test}' for item '{item_name}'"
                )
                try:
                    remove_btn = parent.find_element(
                        By.XPATH, f".//button[@data-test='{data_test}']"
                    )
                    prev_count = self.get_cart_count()
                    remove_btn.click()
                    logger.info(
                        f"[remove_item_by_name] Clicked remove button for '{item_name}'"
                    )
                    try:
                        WebDriverWait(self.driver, 5).until(
                            lambda d: self.get_cart_count() == max(prev_count - 1, 0)
                        )
                        logger.info(
                            f"[remove_item_by_name] Cart count updated to {self.get_cart_count()} after remove."
                        )
                        return True
                    except selenium.common.exceptions.TimeoutException:
                        logger.warning(
                            f"[remove_item_by_name] Cart count did not update after removing '{item_name}'."
                        )
                        return False
                except Exception as e:
                    logger.warning(
                        f"[remove_item_by_name] Could not find/click remove button for '{item_name}': {e}"
                    )
                    return False
        logger.warning(f"[remove_item_by_name] Item '{item_name}' not found on page")
        return False

    def get_cart_count(self):
        """Return the number of items in the cart badge."""
        if self.is_visible(*self.CART_BADGE):
            return int(self.find(*self.CART_BADGE).text)
        return 0

    def go_to_cart(self):
        """Navigate to the cart page."""
        self.click(*self.CART_LINK)
