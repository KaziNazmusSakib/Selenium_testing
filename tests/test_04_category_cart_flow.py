# tests/test_04_category_cart_flow.py
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
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

            # 1) select category (optional)
        self.assertTrue(self.filters.is_visible(self.filters.CATEGORY_FILTERS))
        self.filters.click_first_category()

        # 2) apply filters
        self.filters.apply_filters()
        time.sleep(5)

        # 3) add products
        self.products.add_first_product_to_cart()
        self.products.add_second_product_to_cart()
        time.sleep(5)

         #3.5 clear filters right after adding products
        self.filters.clear_filters()
        time.sleep(5)
        
        # 4) remove more than one from cart
        self.cart.remove_multiple_items()
        time.sleep(5)

        # handle confirm('Are you sure?') alert
        try:
            alert = self.driver.switch_to.alert
            if "Are you sure" in alert.text:
                alert.accept()
        except NoAlertPresentException:
            pass

        # 5) checkout
        cart_el = self.driver.find_element(*self.cart.CART)
        self.assertTrue(cart_el.is_displayed())
        self.cart.checkout()
        time.sleep(5)

 



    def tearDown(self):
        time.sleep(6)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
