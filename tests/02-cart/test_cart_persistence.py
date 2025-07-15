import pytest
import logging
from src.pages.cart_page import CartPage
from src.pages.products_page import ProductsPage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)

ITEMS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]


@pytest.mark.usefixtures("driver")
def test_cart_persistence_after_refresh(login_and_go_to_products):
    """
    Description: Test that the cart retains items after a page refresh.
    Expected Result: The item remains in the cart after refreshing the page.
    """
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    products_page.driver.refresh()
    assert products_page.get_cart_count() == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert ITEMS[0] in cart_page.get_cart_items()


@pytest.mark.usefixtures("driver")
def test_cart_persistence_after_navigation(login_and_go_to_products):
    """
    Description: Test that the cart retains items after navigating away and back to the products page.
    Expected Result: The item remains in the cart after navigation.
    """
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[1])
    products_page.driver.get("https://www.saucedemo.com/inventory.html")
    assert products_page.get_cart_count() == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert ITEMS[1] in cart_page.get_cart_items()


def test_continue_shopping_from_cart(login_and_go_to_products):
    """
    Description: Test the 'Continue Shopping' button from the cart page.
    Expected Result: User is returned to the products page and the cart retains its items.
    """
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_page.find(*CartPage.CONTINUE_SHOPPING).click()
    assert "inventory" in products_page.driver.current_url
    assert products_page.get_cart_count() == 1


def test_checkout_and_return_to_cart(login_and_go_to_products):
    """
    Description: Test that items remain in the cart after starting checkout and returning to the cart page.
    Expected Result: The item remains in the cart after visiting the checkout page and returning.
    """
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_page.find(*CartPage.CHECKOUT_BUTTON).click()
    # Go back to cart
    products_page.driver.get(CartPage.URL)
    assert ITEMS[0] in cart_page.get_cart_items()


def test_cart_persistence_after_clearing_cookies(login_and_go_to_products):
    """
    Description: Test cart behavior after clearing cookies and refreshing.
    Expected Result: The cart is emptied or the user is logged out after cookies are cleared and the page is refreshed.
    """
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    products_page.driver.delete_all_cookies()
    products_page.driver.refresh()
    # Should be logged out or cart should be empty
    assert (
        products_page.get_cart_count() == 0
        or "login" in products_page.driver.current_url
    )
