# Assignment 7: Restructure the login test using Page Object Model.
# Keep locators/actions in the page class and assertions in the test.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    # Store page locators.
    USER = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    # Perform the login action.
    def login(self, username, password):
        self.driver.find_element(*self.USER).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()

# Start browser and run the test.
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
LoginPage(driver).login("standard_user", "secret_sauce")

# Keep the assertion outside the page class.
assert "/inventory.html" in driver.current_url

time.sleep(5)
# Close browser.
driver.quit()