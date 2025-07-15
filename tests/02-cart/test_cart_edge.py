import pytest
import logging
import random
from src.pages.cart_page import CartPage
from src.pages.products_page import ProductsPage
from src.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
def test_remove_item_not_in_cart(login_and_go_to_products):
    """
    Description: Test removing an item that is not in the cart.
    Expected Result: The remove action returns False and the cart remains empty.
    """
    logger.info("[test_remove_item_not_in_cart] Starting test: remove item not in cart")
    products_page = login_and_go_to_products
    item = ITEMS[4]
    removed = products_page.remove_item_by_name(item)
    logger.info(
        f"[test_remove_item_not_in_cart] Attempted to remove {item}, removed={removed}"
    )
    assert not removed
    logger.info("[test_remove_item_not_in_cart] Remove returned False as expected")
    assert products_page.get_cart_count() == 0
    logger.info("[test_remove_item_not_in_cart] Cart count is 0. Test passed.")


@pytest.mark.cart
@pytest.mark.slow
def test_add_all_items_and_remove_all(login_and_go_to_products):
    """
    Description: Test adding all items to the cart and then removing all of them.
    Expected Result: All items are added and then removed, resulting in an empty cart.
    """
    logger.info(
        "[test_add_all_items_and_remove_all] Starting test: add all and remove all"
    )
    products_page = login_and_go_to_products
    for idx, item in enumerate(ITEMS):
        logger.info(f"[test_add_all_items_and_remove_all] Adding item: {item}")
        assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == idx + 1
        )
    assert products_page.get_cart_count() == len(ITEMS)
    logger.info(
        f"[test_add_all_items_and_remove_all] Cart count after adds: {products_page.get_cart_count()}"
    )
    for idx, item in enumerate(ITEMS[::-1]):
        logger.info(f"[test_add_all_items_and_remove_all] Removing item: {item}")
        assert products_page.remove_item_by_name(item), f"Failed to remove item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == len(ITEMS) - (idx + 1)
        )
    assert products_page.get_cart_count() == 0
    logger.info("[test_add_all_items_and_remove_all] Cart count is 0 after removes")
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    cart_items = cart_page.get_cart_items()
    logger.info(
        f"[test_add_all_items_and_remove_all] Cart items after removes: {cart_items}"
    )
    assert cart_page.is_cart_empty()
    logger.info("[test_add_all_items_and_remove_all] Cart is empty. Test passed.")


@pytest.mark.cart
@pytest.mark.slow
def test_add_remove_random_order(login_and_go_to_products):
    """
    Description: Test adding and removing items in random order.
    Expected Result: All items are added and then removed in random order, resulting in an empty cart.
    """
    logger.info("[test_add_remove_random_order] Starting test: add/remove random order")
    products_page = login_and_go_to_products
    items = ITEMS[:]
    random.shuffle(items)
    for idx, item in enumerate(items):
        logger.info(f"[test_add_remove_random_order] Adding item: {item}")
        assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == idx + 1
        )
    assert products_page.get_cart_count() == len(ITEMS)
    logger.info(
        f"[test_add_remove_random_order] Cart count after adds: {products_page.get_cart_count()}"
    )
    random.shuffle(items)
    for idx, item in enumerate(items):
        logger.info(f"[test_add_remove_random_order] Removing item: {item}")
        assert products_page.remove_item_by_name(item), f"Failed to remove item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == len(ITEMS) - (idx + 1)
        )
    assert products_page.get_cart_count() == 0
    logger.info(
        "[test_add_remove_random_order] Cart count is 0 after removes. Test passed."
    )


@pytest.mark.cart
def test_remove_item_twice(login_and_go_to_products):
    """
    Description: Test removing the same item twice.
    Expected Result: The first removal succeeds, the second returns False, and the cart is empty.
    """
    logger.info("[test_remove_item_twice] Starting test: remove item twice")
    products_page = login_and_go_to_products
    products_page.add_item_by_name(ITEMS[0])
    logger.info(f"[test_remove_item_twice] Removing item: {ITEMS[0]}")
    products_page.remove_item_by_name(ITEMS[0])
    logger.info(f"[test_remove_item_twice] Removing item again: {ITEMS[0]}")
    removed_again = products_page.remove_item_by_name(ITEMS[0])
    logger.info(f"[test_remove_item_twice] Second remove returned: {removed_again}")
    assert not removed_again
    assert products_page.get_cart_count() == 0
    logger.info("[test_remove_item_twice] Cart count is 0. Test passed.")


@pytest.mark.cart
def test_cart_badge_not_visible_when_empty(login_and_go_to_products):
    """
    Description: Test that the cart badge is not visible when the cart is empty.
    Expected Result: The cart badge element is not visible when there are no items in the cart.
    """
    logger.info(
        "[test_cart_badge_not_visible_when_empty] Starting test: badge not visible when empty"
    )
    products_page = login_and_go_to_products
    assert products_page.get_cart_count() == 0
    logger.info("[test_cart_badge_not_visible_when_empty] Cart count is 0")
    visible = products_page.is_visible(*ProductsPage.CART_BADGE)
    logger.info(f"[test_cart_badge_not_visible_when_empty] Badge visible: {visible}")
    assert not visible
    logger.info(
        "[test_cart_badge_not_visible_when_empty] Badge not visible. Test passed."
    )


@pytest.mark.cart
@pytest.mark.slow
def test_cart_badge_updates_each_action(login_and_go_to_products):
    """
    Description: Test that the cart badge updates correctly after each add/remove action.
    Expected Result: The cart badge count increases with each add and decreases with each remove, reflecting the correct number of items.
    """
    logger.info(
        "[test_cart_badge_updates_each_action] Starting test: badge updates each action"
    )
    products_page = login_and_go_to_products
    for i, item in enumerate(ITEMS[:3], 1):
        logger.info(f"[test_cart_badge_updates_each_action] Adding item: {item}")
        assert products_page.add_item_by_name(item), f"Failed to add item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == i
        )
        count = products_page.get_cart_count()
        logger.info(
            f"[test_cart_badge_updates_each_action] Cart count after add: {count}"
        )
        assert count == i
    for i, item in enumerate(reversed(ITEMS[:3]), 1):
        logger.info(f"[test_cart_badge_updates_each_action] Removing item: {item}")
        assert products_page.remove_item_by_name(item), f"Failed to remove item: {item}"
        WebDriverWait(products_page.driver, 5).until(
            lambda d: products_page.get_cart_count() == 3 - i
        )
        count = products_page.get_cart_count()
        logger.info(
            f"[test_cart_badge_updates_each_action] Cart count after remove: {count}"
        )
        assert count == 3 - i
    logger.info(
        "[test_cart_badge_updates_each_action] Badge updated correctly. Test passed."
    )
