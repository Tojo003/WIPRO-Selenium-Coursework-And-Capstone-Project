# Assignment 6: Work with an iframe and a new browser tab.
# Switch into the iframe, type text, then switch to a new tab and back.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome.
driver = webdriver.Chrome()

# Open iframe page.
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch into the TinyMCE iframe.
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
)
driver.switch_to.frame(iframe)

# Find the editable body inside the iframe.
editor = driver.find_element(By.TAG_NAME, "body")

# Select existing text and type new text.
editor.send_keys(Keys.CONTROL, "a")
editor.send_keys("Hello")

# Return to the main page.
driver.switch_to.default_content()

# Open the multiple-windows page.
driver.get("https://the-internet.herokuapp.com/windows")

# Save the original window.
original_window = driver.current_window_handle

# Open the new tab.
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Wait for the new tab.
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Switch to the new tab.
driver.switch_to.window(driver.window_handles[-1])

# Print the new tab title.
print(driver.title)

# Close the new tab.
driver.close()

# Return to the original tab.
driver.switch_to.window(original_window)

# Close the browser.
driver.quit()