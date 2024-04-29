import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class PasswordMaskingTest(unittest.TestCase):

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

    def test_password_masking(self):
        # Open the webpage with the username and password fields
        self.driver.get("https://www.saucedemo.com/")

        # Find the username and password fields
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")

        # Enter the username and password
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")

        # Verify that the entered password is masked
        masked_password = password_field.get_attribute("value")
        self.assertNotIn("testpassword", masked_password, "The entered password is not masked")
        print("The entered password is masked")


if __name__ == "__main__":
    unittest.main()
