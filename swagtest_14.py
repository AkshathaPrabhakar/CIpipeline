import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutTest(unittest.TestCase):

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

    def test_logout(self):
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

        # Wait for the page to load and find the menu icon
        wait = WebDriverWait(self.driver, 10)
        menu_icon = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))

        # Click on the menu icon
        menu_icon.click()

        # Find and click on the logout link
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()

        # Check if the URL is redirected after logout
        redirected_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/"
        
        if redirected_url == expected_url:
            print("Logout successful")
        else:
            print("Logout unsuccessful")


if __name__ == "__main__":
    unittest.main()
