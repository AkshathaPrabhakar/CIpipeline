import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class UsernameFieldTest(unittest.TestCase):

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

    def test_username_field(self):
        # Open the Sauce Demo login page
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the username field
        username_field = self.driver.find_element(By.ID, "user-name")

        # Check if the username field is displayed and enabled
        if username_field.is_displayed() and username_field.is_enabled():
            result = "Username field has been recognized"
        else:
            result = "Username field has not been recognized"

        # Print the result
        print("Username field check result:", result)

        # Assert the result
        self.assertEqual(result, "Username field has been recognized", "The username field is not displayed or enabled")


if __name__ == "__main__":
    unittest.main()
