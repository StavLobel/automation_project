import os
import pytest
from src.pages.login_page import LoginPage


SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")


@pytest.mark.usefixtures("driver")
def test_login_valid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(SAUCE_USERNAME, SAUCE_PASSWORD)
    # After successful login, URL should change
    assert "inventory" in driver.current_url


@pytest.mark.usefixtures("driver")
def test_login_invalid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid_user", "wrong_pass")
    error = login_page.get_error_message()
    assert error is not None
    assert (
        "Username and password do not match" in error
        or "do not match" in error
        or "Epic sadface" in error
    )


def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")
    error = login_page.get_error_message()
    assert error is not None
    assert "Username is required" in error or "Epic sadface" in error


def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "somepassword")
    error = login_page.get_error_message()
    assert error is not None
    assert "Username is required" in error or "Epic sadface" in error


def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("someuser", "")
    error = login_page.get_error_message()
    assert error is not None
    assert "Password is required" in error or "Epic sadface" in error


def test_login_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", SAUCE_PASSWORD)
    error = login_page.get_error_message()
    assert error is not None
    assert "locked out" in error.lower() or "Epic sadface" in error


def test_login_invalid_characters(driver):
    login_page = LoginPage(driver)
    login_page.load()
    # Try special characters in username and password
    login_page.login("!@#$%^&*()", "<script>alert(1)</script>")
    error = login_page.get_error_message()
    assert error is not None
    assert (
        "do not match" in error
        or "Epic sadface" in error
        or "Username and password do not match" in error
    )
