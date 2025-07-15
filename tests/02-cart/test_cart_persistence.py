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


@pytest.mark.cart
@pytest.mark.slow
def test_cart_persistence_after_refresh(login_and_go_to_products):
    """
    Description: Test that the cart retains items after a page refresh.
    Expected Result: The item remains in the cart after refreshing the page.
    """
    logger.info(
        "[test_cart_persistence_after_refresh] Starting test: persistence after refresh"
    )
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    logger.info(f"[test_cart_persistence_after_refresh] Added item: {ITEMS[0]}")
    products_page.driver.refresh()
    logger.info("[test_cart_persistence_after_refresh] Page refreshed")
    count = products_page.get_cart_count()
    logger.info(
        f"[test_cart_persistence_after_refresh] Cart count after refresh: {count}"
    )
    assert count == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_cart_persistence_after_refresh] Cart items: {cart_items}")
    assert ITEMS[0] in cart_items
    logger.info(
        "[test_cart_persistence_after_refresh] Item found in cart. Test passed."
    )


@pytest.mark.cart
@pytest.mark.slow
def test_cart_persistence_after_navigation(login_and_go_to_products):
    """
    Description: Test that the cart retains items after navigating away and back to the products page.
    Expected Result: The item remains in the cart after navigation.
    """
    logger.info(
        "[test_cart_persistence_after_navigation] Starting test: persistence after navigation"
    )
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[1])
    logger.info(f"[test_cart_persistence_after_navigation] Added item: {ITEMS[1]}")
    products_page.driver.get("https://www.saucedemo.com/inventory.html")
    logger.info(
        "[test_cart_persistence_after_navigation] Navigated back to inventory page"
    )
    count = products_page.get_cart_count()
    logger.info(
        f"[test_cart_persistence_after_navigation] Cart count after navigation: {count}"
    )
    assert count == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_cart_persistence_after_navigation] Cart items: {cart_items}")
    assert ITEMS[1] in cart_items
    logger.info(
        "[test_cart_persistence_after_navigation] Item found in cart. Test passed."
    )


@pytest.mark.cart
@pytest.mark.slow
def test_continue_shopping_from_cart(login_and_go_to_products):
    """
    Description: Test the 'Continue Shopping' button from the cart page.
    Expected Result: User is returned to the products page and the cart retains its items.
    """
    logger.info(
        "[test_continue_shopping_from_cart] Starting test: continue shopping from cart"
    )
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    logger.info(f"[test_continue_shopping_from_cart] Added item: {ITEMS[0]}")
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_page.find(*CartPage.CONTINUE_SHOPPING).click()
    logger.info("[test_continue_shopping_from_cart] Clicked continue shopping")
    url = products_page.driver.current_url
    logger.info(f"[test_continue_shopping_from_cart] Current URL: {url}")
    assert "inventory" in url
    count = products_page.get_cart_count()
    logger.info(
        f"[test_continue_shopping_from_cart] Cart count after continue shopping: {count}"
    )
    assert count == 1
    logger.info("[test_continue_shopping_from_cart] Test passed.")


@pytest.mark.cart
@pytest.mark.slow
def test_checkout_and_return_to_cart(login_and_go_to_products):
    """
    Description: Test that items remain in the cart after starting checkout and returning to the cart page.
    Expected Result: The item remains in the cart after visiting the checkout page and returning.
    """
    logger.info(
        "[test_checkout_and_return_to_cart] Starting test: checkout and return to cart"
    )
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    logger.info(f"[test_checkout_and_return_to_cart] Added item: {ITEMS[0]}")
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_page.find(*CartPage.CHECKOUT_BUTTON).click()
    logger.info("[test_checkout_and_return_to_cart] Clicked checkout button")
    products_page.driver.get(CartPage.URL)
    logger.info("[test_checkout_and_return_to_cart] Navigated back to cart page")
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_checkout_and_return_to_cart] Cart items: {cart_items}")
    assert ITEMS[0] in cart_items
    logger.info("[test_checkout_and_return_to_cart] Item found in cart. Test passed.")


@pytest.mark.cart
@pytest.mark.slow
def test_cart_persistence_after_clearing_cookies(login_and_go_to_products):
    """
    Description: Test cart behavior after clearing cookies and refreshing.
    Expected Result: The cart is emptied or the user is logged out after cookies are cleared and the page is refreshed.
    """
    logger.info(
        "[test_cart_persistence_after_clearing_cookies] Starting test: persistence after clearing cookies"
    )
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    logger.info(
        f"[test_cart_persistence_after_clearing_cookies] Added item: {ITEMS[0]}"
    )
    products_page.driver.delete_all_cookies()
    logger.info("[test_cart_persistence_after_clearing_cookies] Deleted all cookies")
    products_page.driver.refresh()
    logger.info("[test_cart_persistence_after_clearing_cookies] Page refreshed")
    count = products_page.get_cart_count()
    url = products_page.driver.current_url
    logger.info(
        f"[test_cart_persistence_after_clearing_cookies] Cart count: {count}, URL: {url}"
    )
    assert count == 0 or "login" in url
    logger.info("[test_cart_persistence_after_clearing_cookies] Test passed.")
