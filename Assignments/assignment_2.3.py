# Assignment 8: Read login test data from CSV and execute multiple test cases.
# Assert the expected result for each username/password combination.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create simple external test data.
data = [
    ("standard_user", "secret_sauce", True),
    ("wrong_user", "wrong_password", False),
]

# Run each data set.
for username, password, valid in data:
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Validate successful or failed login.
    assert ("/inventory.html" in driver.current_url) == valid
    driver.quit()