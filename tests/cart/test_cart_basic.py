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
def test_cart_badge_updates(login_and_go_to_products):
    products_page = login_and_go_to_products
    assert products_page.get_cart_count() == 0
    products_page.add_item_by_name(ITEMS[2])
    assert products_page.get_cart_count() == 1
    products_page.add_item_by_name(ITEMS[3])
    assert products_page.get_cart_count() == 2
    products_page.remove_item_by_name(ITEMS[2])
    assert products_page.get_cart_count() == 1
    products_page.remove_item_by_name(ITEMS[3])
    assert products_page.get_cart_count() == 0


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


@pytest.mark.usefixtures("driver")
def test_remove_all_items(login_and_go_to_products):
    products_page = login_and_go_to_products
    for item in ITEMS[:3]:
        products_page.add_item_by_name(item)
    for item in ITEMS[:3]:
        products_page.remove_item_by_name(item)
    assert products_page.get_cart_count() == 0
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert cart_page.is_cart_empty()


@pytest.mark.usefixtures("driver")
def test_rapid_add_remove(login_and_go_to_products):
    products_page = login_and_go_to_products
    item = ITEMS[5]
    for _ in range(5):
        products_page.add_item_by_name(item)
        products_page.remove_item_by_name(item)
    assert products_page.get_cart_count() == 0


@pytest.mark.usefixtures("driver")
def test_cart_empty_state(login_and_go_to_products):
    products_page = login_and_go_to_products
    products_page.go_to_cart()
    cart_page = CartPage(products_page.driver)
    assert cart_page.is_cart_empty()
