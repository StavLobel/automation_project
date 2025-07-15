# tests/cart/test_cart_basic.py
# Basic cart functionality tests for the Swag Labs demo app

import pytest
import logging
from src.pages.cart_page import CartPage
from src.pages.products_page import ProductsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

# List of product names used in cart tests
ITEMS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]


@pytest.mark.cart
@pytest.mark.smoke
def test_add_single_item_to_cart(login_and_go_to_products):
    """
    Description: Test adding a single item to the cart and verifying it appears in the cart.
    Expected Result: The item is added to the cart and appears in the cart items list.
    """
    logger.info("[test_add_single_item_to_cart] Starting test: add single item")
    products_page = login_and_go_to_products
    item = ITEMS[0]
    logger.info(f"[test_add_single_item_to_cart] Adding item: {item}")
    assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
    assert products_page.get_cart_count() == 1
    logger.info("[test_add_single_item_to_cart] Cart count is 1 after add")
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_add_single_item_to_cart] Cart items: {cart_items}")
    assert item in cart_items
    logger.info("[test_add_single_item_to_cart] Item found in cart. Test passed.")


@pytest.mark.cart
def test_add_multiple_items_to_cart(login_and_go_to_products):
    """
    Description: Test adding multiple items to the cart and verifying all appear in the cart.
    Expected Result: All added items appear in the cart items list.
    """
    logger.info("[test_add_multiple_items_to_cart] Starting test: add multiple items")
    products_page = login_and_go_to_products
    for item in ITEMS[:3]:
        logger.info(f"[test_add_multiple_items_to_cart] Adding item: {item}")
        assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
    assert products_page.get_cart_count() == 3
    logger.info("[test_add_multiple_items_to_cart] Cart count is 3 after adds")
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_add_multiple_items_to_cart] Cart items: {cart_items}")
    for item in ITEMS[:3]:
        assert item in cart_items
        logger.info(f"[test_add_multiple_items_to_cart] {item} found in cart.")
    logger.info(
        "[test_add_multiple_items_to_cart] All items found in cart. Test passed."
    )


@pytest.mark.cart
def test_remove_item_from_cart(login_and_go_to_products):
    """
    Description: Test removing an item from the cart and verifying it no longer appears.
    Expected Result: The removed item does not appear in the cart items list.
    """
    logger.info("[test_remove_item_from_cart] Starting test: remove item")
    products_page = login_and_go_to_products
    item = ITEMS[1]
    logger.info(f"[test_remove_item_from_cart] Adding item: {item}")
    assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
    logger.info(f"[test_remove_item_from_cart] Removing item: {item}")
    assert products_page.remove_item_by_name(item), f"Failed to remove item: {item}"
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_remove_item_from_cart] Cart items after remove: {cart_items}")
    assert item not in cart_items
    logger.info("[test_remove_item_from_cart] Item not found in cart. Test passed.")


@pytest.mark.cart
def test_add_same_item_multiple_times(login_and_go_to_products):
    """
    Description: Test adding the same item multiple times does not duplicate it in the cart.
    Expected Result: The item appears only once in the cart items list, regardless of how many times it is added.
    """
    logger.info(
        "[test_add_same_item_multiple_times] Starting test: add same item multiple times"
    )
    products_page = login_and_go_to_products
    item = ITEMS[0]
    logger.info(f"[test_add_same_item_multiple_times] Adding item: {item}")
    assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
    WebDriverWait(products_page.driver, 5).until(
        lambda d: products_page.get_cart_count() == 1
    )
    logger.info(f"[test_add_same_item_multiple_times] Adding item again: {item}")
    assert not products_page.add_item_by_name(
        item
    ), f"Second add should fail for item: {item}"
    WebDriverWait(products_page.driver, 5).until(
        lambda d: products_page.get_cart_count() == 1
    )
    assert products_page.get_cart_count() == 1
    logger.info(
        "[test_add_same_item_multiple_times] Cart count is 1 after duplicate adds"
    )
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(f"[test_add_same_item_multiple_times] Cart items: {cart_items}")
    assert cart_items.count(item) == 1
    logger.info(
        "[test_add_same_item_multiple_times] Item appears only once in cart. Test passed."
    )
