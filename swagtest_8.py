import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShoppingCartTest(unittest.TestCase):

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

    def test_shopping_cart(self):
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

        # Find the "Add to Cart" button for the inventory item "Sauce Labs Bike Light" using its ID
        add_to_cart_button_id = "add-to-cart-sauce-labs-bike-light"
        
        # Wait for the "Add to Cart" button to be clickable
        wait = WebDriverWait(self.driver, 10)
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, add_to_cart_button_id)))
        
        # Click on the "Add to Cart" button
        add_to_cart_button.click()
        
        # Wait for the shopping cart badge to appear after adding the item to the cart
        shopping_cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        
        # Click on the shopping cart badge to view the cart
        shopping_cart_badge.click()
        
        # Verify if the "Sauce Labs Bike Light" item is added to the cart by checking if its name is displayed in the cart
        item_name = "Sauce Labs Bike Light"
        item_in_cart = self.driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")
        
        # Print message based on verification result
        if item_in_cart.is_displayed():
            print("Item verified and correctly added to cart")
        else:
            print("Items added to cart did not match")


if __name__ == "__main__":
    unittest.main()
