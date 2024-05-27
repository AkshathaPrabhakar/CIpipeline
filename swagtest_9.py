import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinkedInIconTest(unittest.TestCase):

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

    def test_linkedin_icon(self):
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
        wait = WebDriverWait(self.driver, 20)
        linkedin_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'linkedin.com/company')]")))
        
        # Assert if the LinkedIn icon is displayed after login
        self.assertTrue(linkedin_icon.is_displayed(), "LinkedIn icon is not present after login")
        
        # Check the href attribute of the LinkedIn icon
        linkedin_url = linkedin_icon.get_attribute("href")
        
        # Assert if the href attribute contains the expected LinkedIn URL
        expected_linkedin_url = "https://www.linkedin.com/company/sauce-labs/"
        self.assertEqual(linkedin_url, expected_linkedin_url, "LinkedIn URL is incorrect")
        
        # Print a message if the LinkedIn icon and its href attribute are found
        print("LinkedIn Icon and href verified")


if __name__ == "__main__":
    unittest.main()
