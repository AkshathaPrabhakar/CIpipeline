import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginTest(unittest.TestCase):

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

    def test_login(self):
        # Open the Sauce Demo login page
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the username and password fields
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")

        # Enter username and password
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        
        # Find and click the login button
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # Check if login is successful by verifying the presence of the products page title
        products_page_title = self.driver.find_element(By.CLASS_NAME, "title").text
        expected_title = "Products"
        
        # Assert if the products page title is as expected
        self.assertEqual(products_page_title, expected_title, "Login was not successful. Products page title not found.")
        
        # Print message for successful login
        print("Login successful!")

if __name__ == "__main__":
    unittest.main()
