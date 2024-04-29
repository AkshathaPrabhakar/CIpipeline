import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class ContentCheckerTest(unittest.TestCase):

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

    def test_check_title(self):
        # Open the Sauce Demo homepage
        self.driver.get("https://www.saucedemo.com/")
        
        # Get the title of the page
        page_title = self.driver.title

        # Check if the title contains the word "Swag"
        if "SwagsPage" in page_title:
            result = "Title of the web page found"
        else:
            result = "Title of the web page not found"

        # Print the result
        print("Title check result:", result)

        # Assert the result
        self.assertEqual(result, "Pass", "The title of the page does not contain the word 'Swag'")


if __name__ == "__main__":
    unittest.main()
