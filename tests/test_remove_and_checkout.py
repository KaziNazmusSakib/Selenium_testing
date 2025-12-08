# tests/test_remove_and_checkout.py
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRemoveAndCheckout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("F:/Projects/Selenium_testing/index.html")
        time.sleep(1)

    def test_remove_items_and_checkout(self):
        driver = self.driver
        # Fill cart with multiple items
        apply_btn = driver.find_element(By.ID, "apply-filters-btn")
        apply_btn.click()
        time.sleep(1)
        add_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart")
        self.assertTrue(len(add_buttons) >= 2)
        add_buttons[0].click()
        add_buttons[1].click()
        time.sleep(1)
        # Remove more than one item
        remove_buttons = driver.find_elements(By.CLASS_NAME, "remove-from-cart")
        self.assertTrue(len(remove_buttons) >= 2)
        remove_buttons[0].click()
        remove_buttons[1].click()
        time.sleep(1)
        # Checkout button
        checkout_btn = driver.find_element(By.ID, "checkout-btn")
        self.assertTrue(checkout_btn.is_enabled())
        checkout_btn.click()
        # Assert cart is empty after checkout, adjust to your behavior
        cart_items = driver.find_element(By.ID, "cart-items")
        self.assertEqual(cart_items.text.strip(), "")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
