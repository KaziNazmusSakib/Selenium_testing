# tests/test_04_category_cart_flow.py
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


class TestCategoryCartFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

        self.login = LoginPage(self.driver)
        self.signup = SignupPage(self.driver)
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)

    def test_category_add_remove_checkout(self):
        self.driver.get("F:/Selenium_testing/index.html")

        # 1) select more than one category (your FiltersPage should do this)
        self.assertTrue(self.filters.is_visible(self.filters.CATEGORY_FILTERS))
        self.filters.click_any_category()         # adjust: make this select multiple if needed
        self.filters.click_any_category()

        # 2) apply filters
        self.filters.apply_filters()
        time.sleep(1)

        # 3) add to cart (more than one product if possible)
        self.products.add_first_product_to_cart()
        self.products.add_first_product_to_cart()  # or add_second_product_to_cart()
        time.sleep(1)

        # 4) remove more than one from cart
        self.cart.remove_first_item()
        self.cart.remove_first_item()
        time.sleep(1)

        # 5) checkout
        self.assertTrue(self.cart.is_visible(self.cart.CART))
        self.cart.checkout()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
