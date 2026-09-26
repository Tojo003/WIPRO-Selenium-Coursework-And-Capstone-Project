# Assignment 1: Navigate to SauceDemo and use ID, NAME, and XPATH locators.
# Login successfully and assert that the URL contains /inventory.html.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
assert "/inventory.html" in driver.current_url

time.sleep(5)

driver.quit()
