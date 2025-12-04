import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class EcommerceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_page_load(self):
        driver = self.driver
        driver.get("F:/Projects/Selenium_testing/index.html")

        # check title
        self.assertIn("Simple E-commerce", driver.title)

        # check product-grid exists
        grid = driver.find_element(By.ID, "product-grid")
        self.assertTrue(grid.is_displayed())

        # click Apply Filters
        apply_btn = driver.find_element(By.ID, "apply-filters-btn")
        apply_btn.click()

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
