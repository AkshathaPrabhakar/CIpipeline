import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInPageTest(unittest.TestCase):

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

    def test_linkedin_page(self):
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

        # Wait for the LinkedIn icon to appear after login
        wait = WebDriverWait(self.driver, 10)
        linkedin_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'linkedin.com/company')]")))
        
        # Click on the LinkedIn icon
        linkedin_icon.click()

        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Wait for the LinkedIn page to load and get its page source
        linkedin_page_source = self.driver.page_source

        # Assert if the content of the page contains the text "LinkedIn"
        self.assertIn("LinkedIn", linkedin_page_source, "LinkedIn page content does not contain 'LinkedIn'")

        # Print a message if the LinkedIn page is opened successfully
        print("LinkedIn page is opened successfully")


if __name__ == "__main__":
    unittest.main()
