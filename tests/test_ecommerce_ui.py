import unittest
from selenium import webdriver
from pages.filters_page import FiltersPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
import time


class EcommerceUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("F:/Projects/Selenium_testing/index.html")
        time.sleep(1)

        # PAGE OBJECTS
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)
        
    # --------------------------------------------------------
    # PAGE LOAD TEST
    # --------------------------------------------------------
    def test_page_title(self):
        self.assertIn("Simple E-commerce", self.driver.title)

    # --------------------------------------------------------
    # ELEMENT EXISTENCE TESTS
    # --------------------------------------------------------
    def test_category_filters_exists(self):
        self.assertTrue(self.filters.is_visible(self.filters.CATEGORY_FILTERS))

    def test_apply_filters_button_exists(self):
        self.assertTrue(self.filters.is_visible(self.filters.APPLY_BTN))

    def test_clear_filters_button_exists(self):
        self.assertTrue(self.filters.is_visible(self.filters.CLEAR_BTN))

    def test_product_grid_exists(self):
        self.assertTrue(self.products.is_visible(self.products.PRODUCT_GRID))

    def test_cart_section_exists(self):
        self.assertTrue(self.cart.is_visible(self.cart.CART))

    def test_cart_items_exists(self):
        self.assertTrue(self.cart.is_visible(self.cart.CART_ITEMS))

    def test_total_price_exists(self):
        self.assertTrue(self.cart.is_visible(self.cart.TOTAL_PRICE))

    def test_checkout_button_exists(self):
        self.assertTrue(self.cart.is_visible(self.cart.CHECKOUT_BTN))

    # --------------------------------------------------------
    # BUTTON CLICKABILITY
    # --------------------------------------------------------
    def test_apply_filters_button_clickable(self):
        self.filters.apply_filters()
        self.assertTrue(True)

    def test_clear_filters_button_clickable(self):
        self.filters.clear_filters()
        self.assertTrue(True)

    # --------------------------------------------------------
    # CART TESTS
    # --------------------------------------------------------
    def test_cart_visible(self):
        self.assertTrue(self.cart.is_visible(self.cart.CART))

    def test_cart_items_default_empty(self):
        self.assertEqual(self.cart.get_items_text().strip(), "")

    def test_checkout_button_clickable(self):
        self.cart.checkout()
        self.assertTrue(True)

    # --------------------------------------------------------
    # PRODUCT GRID TESTS
    # --------------------------------------------------------
    def test_product_grid_visible(self):
        self.assertTrue(self.products.is_visible(self.products.PRODUCT_GRID))

    def test_product_grid_initially_empty(self):
        self.assertEqual(self.products.grid_text().strip(), "")

    def test_product_grid_after_apply_filters(self):
        self.filters.apply_filters()
        time.sleep(1)
        self.assertTrue(len(self.products.grid_text()) >= 0)

    # --------------------------------------------------------

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
