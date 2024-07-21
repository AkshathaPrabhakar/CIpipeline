import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutFormTest(unittest.TestCase):

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

    def test_form_page(self):
        # Open the Sauce Demo login page
        self.driver.get("https://www.saucedemo.com/")
        
        # Find the username and password fields and enter credentials
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        
        # Find and click the login button
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # Wait for the page to load and find the shopping cart button
        wait = WebDriverWait(self.driver, 10)
        shopping_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))

        # Wait for 5 seconds
        time.sleep(5)

        # Click on the shopping cart button
        shopping_cart_button.click()

        # Wait for the "Checkout" button and click on it
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Check if the form page is loaded by verifying the presence of first name, last name, and postal code fields
        try:
            first_name_field = self.driver.find_element(By.ID, "first-name")
            last_name_field = self.driver.find_element(By.ID, "last-name")
            postal_code_field = self.driver.find_element(By.ID, "postal-code")
            print("The checkout form fields are identified properly")
        except:
            print("Checkout form fields are not identified")


if __name__ == "__main__":
    unittest.main()
