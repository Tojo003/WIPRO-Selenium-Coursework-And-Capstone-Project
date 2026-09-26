# BDD Assignment 1: Create a simple Selenium Behave scenario.
# Open SauceDemo and verify the page title.

from selenium import webdriver

# Create the browser before the scenario.
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

# Close the browser after the scenario.
def after_scenario(context, scenario):
    context.driver.quit()
