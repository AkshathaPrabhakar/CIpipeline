import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class InvalidLoginTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver for Chrome with options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--no-sandbox")  # Disable sandboxing
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

    def test_invalid_login(self):
        # Open the Sauce Demo login page
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the username and password fields
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")

        # Enter incorrect username and password
        username_field.send_keys("aaaaa")
        password_field.send_keys("xxxxxxxx")
        
        # Find and click the login button
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # Check if error message is displayed
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
            expected_error_message = "Epic sadface: Username and password do not match any user in this service"

            # Assert if the error message is as expected
            self.assertEqual(error_message, expected_error_message, "Error message is not displayed or incorrect")

            print("Error message identified: ", error_message)
        except NoSuchElementException:
            print("Could not identify error message")


if __name__ == "__main__":
    unittest.main()
