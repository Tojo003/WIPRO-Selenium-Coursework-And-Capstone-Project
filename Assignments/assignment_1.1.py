# Assignment 1: Navigate to SauceDemo and use ID, NAME, and XPATH locators.
# Login successfully and assert that the URL contains /inventory.html.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Start Chrome.
driver = webdriver.Chrome()

# Open SauceDemo.
driver.get("https://www.saucedemo.com/")

# Fill username using ID.
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Fill password using NAME.
driver.find_element(By.NAME, "password").send_keys("secret_sauce")

# Click login using XPATH.
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Verify successful login.
assert "/inventory.html" in driver.current_url

time.sleep(5)

# Close browser.
driver.quit()
