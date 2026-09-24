import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browsername = "firefox"

if browsername.lower() == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'firefox'.")


try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    name_field = driver.find_element(By.CSS_SELECTOR, "input[id^='nam']")
    name_field.send_keys("Selenium User")

    email_field = driver.find_element(By.CSS_SELECTOR, "input[id$='ail']")
    email_field.send_keys("user@example.com")

    phone_field = driver.find_element(By.CSS_SELECTOR, "input[id*='hon']")
    phone_field.send_keys("1234567890")

    text_area = driver.find_element(By.CSS_SELECTOR, "textarea[id='textarea']")
    text_area.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempus arcu in molestie tempus. Nullam vehicula lorem eget erat molestie, eu facilisis leo bibendum. Donec mauris nibh, viverra in ex ut, egestas congue augue. Duis sed tristique augue, lacinia laoreet arcu. Cras condimentum pharetra nisi sit amet hendrerit. Sed nec. ")

    male_radio = driver.find_element(By.CSS_SELECTOR, "input[id*='mal'][type='radio']")
    male_radio.click()

    dynamic_button = driver.find_element(By.CSS_SELECTOR, "button[name^='star']")
    dynamic_button.click()

    option_1 = driver.find_element(By.CSS_SELECTOR, "input[id='monday']")
    option_1.click()
    option_2 = driver.find_element(By.CSS_SELECTOR, "input[id='tuesday']")
    option_2.click()
    option_3 = driver.find_element(By.CSS_SELECTOR, "input[id='saturday']")
    option_3.click()

    time.sleep(9)
finally:
    driver.quit()
