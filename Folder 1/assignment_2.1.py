# Assignment 7: Create a basic unittest test case with setup and teardown.
# Verify that SauceDemo opens correctly.

import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):
    # Create the browser before each test.
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Run the test.
    def test_login_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.assertIn("Swag Labs", self.driver.title)

    # Close the browser after each test.
    def tearDown(self):
        self.driver.quit()

# Run the unittest suite.
if __name__ == "__main__":
    unittest.main()