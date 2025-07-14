import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage

load_dotenv()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


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
