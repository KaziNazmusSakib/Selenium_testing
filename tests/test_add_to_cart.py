# tests/test_add_to_cart.py
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAddToCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("F:/Projects/Selenium_testing/index.html")
        time.sleep(1)

    def test_add_items_to_cart(self):
        driver = self.driver
        cart_items = driver.find_element(By.ID, "cart-items")
        self.assertEqual(cart_items.text.strip(), "")
        # Example: click first two "Add to cart" buttons on product grid
        apply_btn = driver.find_element(By.ID, "apply-filters-btn")
        apply_btn.click()
        time.sleep(1)
        add_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart")
        self.assertTrue(len(add_buttons) >= 1)
        add_buttons[0].click()
        time.sleep(1)
        self.assertNotEqual(cart_items.text.strip(), "")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
