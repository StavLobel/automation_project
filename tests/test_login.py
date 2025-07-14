import os
import pytest
import logging
from src.pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")


@pytest.mark.usefixtures("driver")
def test_login_valid(driver):
    logger.info("[test_login_valid] Starting valid login test")
    logger.info(
        f"[test_login_valid] Using credentials: username='{SAUCE_USERNAME}', password='***'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_valid] Loaded login page")
    login_page.login(SAUCE_USERNAME, SAUCE_PASSWORD)
    logger.info("[test_login_valid] Submitted login form with valid credentials")
    assert "inventory" in driver.current_url
    logger.info("[test_login_valid] Login successful, inventory page loaded")


@pytest.mark.usefixtures("driver")
def test_login_invalid(driver):
    username = "invalid_user"
    password = "wrong_pass"
    logger.info("[test_login_invalid] Starting invalid login test")
    logger.info(
        f"[test_login_invalid] Using credentials: username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_invalid] Loaded login page")
    login_page.login(username, password)
    logger.info("[test_login_invalid] Submitted login form with invalid credentials")
    error = login_page.get_error_message()
    logger.info(f"[test_login_invalid] Error message: {error}")
    assert (
        "Username and password do not match" in error
        or "do not match" in error
        or "Epic sadface" in error
    )
    logger.info("[test_login_invalid] Error message assertion passed")


def test_login_empty_fields(driver):
    username = ""
    password = ""
    logger.info("[test_login_empty_fields] Starting empty fields login test")
    logger.info(
        f"[test_login_empty_fields] Using credentials: username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_empty_fields] Loaded login page")
    login_page.login(username, password)
    logger.info("[test_login_empty_fields] Submitted login form with empty fields")
    error = login_page.get_error_message()
    logger.info(f"[test_login_empty_fields] Error message: {error}")
    assert "Username is required" in error or "Epic sadface" in error
    logger.info("[test_login_empty_fields] Error message assertion passed")


def test_login_empty_username(driver):
    username = ""
    password = "somepassword"
    logger.info("[test_login_empty_username] Starting empty username login test")
    logger.info(
        f"[test_login_empty_username] Using credentials: username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_empty_username] Loaded login page")
    login_page.login(username, password)
    logger.info("[test_login_empty_username] Submitted login form with empty username")
    error = login_page.get_error_message()
    logger.info(f"[test_login_empty_username] Error message: {error}")
    assert "Username is required" in error or "Epic sadface" in error
    logger.info("[test_login_empty_username] Error message assertion passed")


def test_login_empty_password(driver):
    username = "someuser"
    password = ""
    logger.info("[test_login_empty_password] Starting empty password login test")
    logger.info(
        f"[test_login_empty_password] Using credentials: username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_empty_password] Loaded login page")
    login_page.login(username, password)
    logger.info("[test_login_empty_password] Submitted login form with empty password")
    error = login_page.get_error_message()
    logger.info(f"[test_login_empty_password] Error message: {error}")
    assert "Password is required" in error or "Epic sadface" in error
    logger.info("[test_login_empty_password] Error message assertion passed")


def test_login_locked_out_user(driver):
    username = "locked_out_user"
    password = SAUCE_PASSWORD
    logger.info("[test_login_locked_out_user] Starting locked out user login test")
    logger.info(
        f"[test_login_locked_out_user] Using credentials: username='{username}', password='***'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_locked_out_user] Loaded login page")
    login_page.login(username, password)
    logger.info(
        "[test_login_locked_out_user] Submitted login form with locked out user"
    )
    error = login_page.get_error_message()
    logger.info(f"[test_login_locked_out_user] Error message: {error}")
    assert "locked out" in error.lower() or "Epic sadface" in error
    logger.info("[test_login_locked_out_user] Error message assertion passed")


def test_login_invalid_characters(driver):
    username = "!@#$%^&*()"
    password = "<script>alert(1)</script>"
    logger.info(
        "[test_login_invalid_characters] Starting invalid characters login test"
    )
    logger.info(
        f"[test_login_invalid_characters] Using credentials: username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.load()
    logger.info("[test_login_invalid_characters] Loaded login page")
    login_page.login(username, password)
    logger.info(
        "[test_login_invalid_characters] Submitted login form with special characters"
    )
    error = login_page.get_error_message()
    logger.info(f"[test_login_invalid_characters] Error message: {error}")
    assert (
        "do not match" in error
        or "Epic sadface" in error
        or "Username and password do not match" in error
    )
    logger.info("[test_login_invalid_characters] Error message assertion passed")
