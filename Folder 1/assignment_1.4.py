# Assignment 4: Trigger an alert, confirm, and prompt.
# Accept the alert, dismiss the confirm, and enter text in the prompt.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Start Chrome.
driver = webdriver.Chrome()

# Open JavaScript alerts page.
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Accept the alert.
driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Alert')]").click()
driver.switch_to.alert.accept()

# Dismiss the confirm.
driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Confirm')]").click()
driver.switch_to.alert.dismiss()

# Enter text into the prompt and accept it.
driver.find_element(By.XPATH, "//button[contains(.,'Click for JS Prompt')]").click()
driver.switch_to.alert.send_keys("Hello")
driver.switch_to.alert.accept()

time.sleep(5)
# Close browser.
driver.quit()