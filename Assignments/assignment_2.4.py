# Assignment 9: Run Selenium with PyTest and generate an HTML report.
# Use a fixture for browser setup and teardown.

import pytest
from selenium import webdriver

# Create and close the browser for each test.
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# Test the SauceDemo page.
def test_login_page(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title