# Assignment 2: Use an explicit wait instead of time.sleep().
# Wait for a dynamic element to become visible and read its text.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome.
driver = webdriver.Chrome()

# Open a page with a delayed element.
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.CSS_SELECTOR, "#start button").click()

# Wait until the result is visible.
result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

# Print the loaded text.
print(result.text)

time.sleep(5)
# Close browser.
driver.quit()