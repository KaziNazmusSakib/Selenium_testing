import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        
        # Check title
        self.assertIn("Python", driver.title)

        # Fix: correct locator
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Community")
        elem.send_keys(Keys.RETURN)

        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
