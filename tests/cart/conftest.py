import os
import pytest
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage


@pytest.fixture(scope="function")
def login_and_go_to_products(driver):
    username = os.getenv("SAUCE_USERNAME")
    password = os.getenv("SAUCE_PASSWORD")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    products_page = ProductsPage(driver)
    assert "inventory" in driver.current_url
    return products_page
