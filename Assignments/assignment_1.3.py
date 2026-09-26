# Assignment 3: Select checkboxes and choose an autocomplete suggestion.
# Verify checkbox state using is_selected().

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome.
driver = webdriver.Chrome()

# Open checkbox page.
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Select both checkboxes.
boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for box in boxes:
    if not box.is_selected():
        box.click()

# Verify all checkboxes are selected.
assert all(box.is_selected() for box in boxes)


time.sleep(5)
# Close browser.
driver.quit()