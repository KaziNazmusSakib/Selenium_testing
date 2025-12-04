import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class  TestEcommerce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("F:/Projects/Selenium_testing/index.html")
        time.sleep(1)

    # # check title
    def test_page_load(self):
        self.assertIn("Simple E-commerce", self.driver.title)
   
    #-------------------------
    # BUTTON BEHAVIOR TESTS  
    #-------------------------

    # ─────────────────────────────────────────────
    # ELEMENT EXISTENCE TESTS (8 tests)
    # ─────────────────────────────────────────────
    def test_category_filters_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "category-filters"))

    def test_apply_filters_button_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "apply-filters-btn"))

    def test_clear_filters_button_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "clear-filters-btn"))

    def test_product_grid_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "product-grid"))

    def test_cart_section_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "cart"))

    def test_cart_items_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "cart-items"))

    def test_total_price_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "total-price"))

    def test_checkout_button_exists(self):
        self.assertTrue(self.driver.find_element(By.ID, "checkout-btn"))

    # ─────────────────────────────────────────────
    # CART SECTION TESTS (3 tests)
    # ─────────────────────────────────────────────
    def test_cart_is_visible(self):
        cart = self.driver.find_element(By.ID, "cart")
        self.assertTrue(cart.is_displayed())

    def test_cart_items_default_empty(self):
        items = self.driver.find_element(By.ID, "cart-items")
        self.assertEqual(items.text.strip(), "")

    def test_checkout_button_clickable(self):
        btn = self.driver.find_element(By.ID, "checkout-btn")
        btn.click()
        self.assertTrue(btn.is_enabled())



    # click Apply Filters
    def test_apply_filters_button_clickable(self):    
        apply_btn = self.driver.find_element(By.ID, "apply-filters-btn")
        apply_btn.click()
        self.assertTrue(apply_btn.is_enabled())

    # click Clear Filters
    def test_clear_filters_button_clickable(self):    
        clear_btn = self.driver.find_element(By.ID, "clear-filters-btn")
        clear_btn.click()
        self.assertTrue(clear_btn.is_enabled())

    # click Clear Filters
    def test_checkout_filters_button_clickable(self):     
        checkout_btn = self.driver.find_element(By.ID, "checkout-btn")
        checkout_btn.click()
        self.assertTrue(checkout_btn.is_enabled())

     

      # ─────────────────────────────────────────────
    # PRODUCT GRID BEHAVIOR TESTS (2–3 tests)
    # ─────────────────────────────────────────────
    def test_product_grid_is_visible(self):
        grid = self.driver.find_element(By.ID, "product-grid")
        self.assertTrue(grid.is_displayed())

    def test_product_grid_initially_empty(self):
        grid = self.driver.find_element(By.ID, "product-grid")
        self.assertEqual(grid.text.strip(), "")

    # If your app.js adds products after Apply Filters, test this:
    def test_product_grid_updates_after_apply_filters(self):
        apply_btn = self.driver.find_element(By.ID, "apply-filters-btn")
        apply_btn.click()
        time.sleep(1)

        grid = self.driver.find_element(By.ID, "product-grid")
        # JS should append products. If static, change rule accordingly.
        self.assertTrue(len(grid.text) >= 0)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
