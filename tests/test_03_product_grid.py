# tests/test_03_product_grid.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.filters_cart_products_locators import (
    FiltersPage,
    CartPage,
    ProductsPage,
)


class TestProductGrid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

        self.login = LoginPage(self.driver)
        self.signup = SignupPage(self.driver)
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)

    def test_product_grid_visible(self):
        self.driver.get("F:/Selenium_testing/index.html")

        self.assertTrue(self.products.is_visible(self.products.PRODUCT_GRID))
        self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, "bg-white")) >= 0)
        self.assertTrue(len(self.driver.find_elements(By.CSS_SELECTOR, "#product-grid > div")) >= 0)

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
