# Assignment 5: Extract data from an HTML table.
# Find the row containing "Smith" and print its Status value.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome.
driver = webdriver.Chrome()

# Open the table page.
driver.get("https://the-internet.herokuapp.com/tables")

# Read all table rows.
rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

# Find Smith's row and print the Status column.
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if "Smith" in cells[1].text:
        print(cells[5].text)
        break

time.sleep(5)
# Close browser.
driver.quit()