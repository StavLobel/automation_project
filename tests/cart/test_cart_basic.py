import pytest
import logging
from src.pages.cart_page import CartPage
from src.pages.products_page import ProductsPage

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
def test_add_single_item_to_cart(login_and_go_to_products):
    products_page = login_and_go_to_products
    item = ITEMS[0]
    logger.info(f"Adding item: {item}")
    products_page.add_item_by_name(item)
    assert products_page.get_cart_count() == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert item in cart_page.get_cart_items()


@pytest.mark.usefixtures("driver")
def test_add_multiple_items_to_cart(login_and_go_to_products):
    products_page = login_and_go_to_products
    for item in ITEMS[:3]:
        logger.info(f"Adding item: {item}")
        products_page.add_item_by_name(item)
    assert products_page.get_cart_count() == 3
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    for item in ITEMS[:3]:
        assert item in cart_page.get_cart_items()


@pytest.mark.usefixtures("driver")
def test_remove_item_from_cart(login_and_go_to_products):
    products_page = login_and_go_to_products
    item = ITEMS[1]
    products_page.add_item_by_name(item)
    assert products_page.get_cart_count() == 1
    products_page.remove_item_by_name(item)
    assert products_page.get_cart_count() == 0
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert item not in cart_page.get_cart_items()


@pytest.mark.usefixtures("driver")
def test_add_same_item_multiple_times(login_and_go_to_products):
    products_page = login_and_go_to_products
    item = ITEMS[0]
    products_page.add_item_by_name(item)
    products_page.add_item_by_name(item)  # Should not duplicate
    assert products_page.get_cart_count() == 1
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert cart_page.get_cart_items().count(item) == 1
