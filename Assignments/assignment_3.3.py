# BDD Assignment 3: Use a Page Object Model with Behave.
# Keep Selenium locators and actions inside the page object.

from selenium.webdriver.common.by import By

class LoginPage:
    # Store the login locators.
    USER = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    # Perform login.
    def login(self, username, password):
        self.driver.find_element(*self.USER).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()
