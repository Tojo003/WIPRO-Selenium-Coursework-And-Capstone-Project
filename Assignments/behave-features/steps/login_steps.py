from behave import given, when, then
from selenium.webdriver.common.by import By

@given("SauceDemo is open")
def open_page(context):
    context.driver.get("https://www.saucedemo.com/")

@when('I login with "{username}" and "{password}"')
def login(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then("the inventory page is displayed")
def verify(context):
    assert "/inventory.html" in context.driver.current_url
