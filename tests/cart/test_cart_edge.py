import pytest
import logging
import random
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


# @pytest.mark.usefixtures("driver")
# def test_remove_item_not_in_cart(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     item = ITEMS[4]
#     removed = products_page.remove_item_by_name(item)
#     assert not removed
#     assert products_page.get_cart_count() == 0


# def test_add_all_items_and_remove_all(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     for item in ITEMS:
#         products_page.add_item_by_name(item)
#     assert products_page.get_cart_count() == len(ITEMS)
#     for item in ITEMS:
#         products_page.remove_item_by_name(item)
#     assert products_page.get_cart_count() == 0
#     products_page.go_to_cart()
#     cart_page = CartPage(products_page.driver)
#     assert cart_page.is_cart_empty()


# def test_add_remove_random_order(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     items = ITEMS[:]
#     random.shuffle(items)
#     for item in items:
#         products_page.add_item_by_name(item)
#     random.shuffle(items)
#     for item in items:
#         products_page.remove_item_by_name(item)
#     assert products_page.get_cart_count() == 0


# def test_remove_item_twice(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     products_page.add_item_by_name(ITEMS[0])
#     products_page.remove_item_by_name(ITEMS[0])
#     # Try to remove again, should not error
#     assert not products_page.remove_item_by_name(ITEMS[0])
#     assert products_page.get_cart_count() == 0


# def test_cart_badge_not_visible_when_empty(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     assert products_page.get_cart_count() == 0
#     # Check if badge element is not visible
#     assert not products_page.is_visible(*ProductsPage.CART_BADGE)


# def test_cart_badge_updates_each_action(login_and_go_to_products):
#     products_page = login_and_go_to_products
#     for i, item in enumerate(ITEMS[:3], 1):
#         products_page.add_item_by_name(item)
#         assert products_page.get_cart_count() == i
#     for i, item in enumerate(reversed(ITEMS[:3]), 1):
#         products_page.remove_item_by_name(item)
#         assert products_page.get_cart_count() == 3 - i
