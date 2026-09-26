# BDD Assignment 2: Use test data with a Behave scenario outline.
# The step definitions use the supplied username and password.

from selenium.webdriver.common.by import By

# Open SauceDemo.
def step_open(context):
    context.driver.get("https://www.saucedemo.com/")

# Enter login credentials.
def step_login(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

# Verify the login result.
def step_verify(context):
    assert "/inventory.html" in context.driver.current_url
