import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginButtonTest(unittest.TestCase):

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

    def test_login_button(self):
        # Open the Sauce Demo homepage
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

        # Check if the login button is displayed and enabled
        if login_button.is_displayed() and login_button.is_enabled():
            result = "Login button has been recognized"
        else:
            result = "Login button has not been recognized"

        # Print the result
        print("Login button check result:", result)

        # Assert the result
        self.assertEqual(result, "Login button has been recognized", "The login button is not displayed or enabled")


if __name__ == "__main__":
    unittest.main()
