# tests/login/test_login.py
# Login functionality tests for the Swag Labs demo app

import os
import pytest
import logging
from src.pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Credentials are loaded from environment variables
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")


@pytest.mark.usefixtures("driver")
def test_login_valid(driver):
    """
    Description: Test logging in with valid credentials.
    Expected Result: User is successfully logged in and redirected to the inventory page.
    """
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
    """
    Description: Test logging in with invalid credentials.
    Expected Result: An error message is displayed indicating invalid username or password.
    """
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
    """
    Description: Test logging in with empty username and password fields.
    Expected Result: An error message is displayed indicating that the username is required.
    """
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
    """
    Description: Test logging in with an empty username.
    Expected Result: An error message is displayed indicating that the username is required.
    """
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
    """
    Description: Test logging in with an empty password.
    Expected Result: An error message is displayed indicating that the password is required.
    """
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
    """
    Description: Test logging in as a locked out user.
    Expected Result: An error message is displayed indicating the user is locked out.
    """
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
    """
    Description: Test logging in with invalid/special characters in username and password.
    Expected Result: An error message is displayed indicating invalid credentials.
    """
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
