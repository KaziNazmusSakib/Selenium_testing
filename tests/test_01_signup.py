# tests/test_01_signup.py
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


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

        self.login = LoginPage(self.driver)
        self.signup = SignupPage(self.driver)
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)

    def test_signup_locators_and_flow(self):
        self.driver.get("F:/Selenium_testing/auth/sign-up.html")

        self.assertTrue(self.signup.is_visible(self.signup.USERNAME))
        self.assertTrue(self.signup.is_visible(self.signup.EMAIL))
        self.assertTrue(self.signup.is_visible(self.signup.PASSWORD))
        self.assertTrue(self.signup.is_visible(self.signup.SIGNUP_BTN))
        self.assertTrue(self.signup.is_visible(self.signup.FORM_TAG))
        self.assertTrue(self.signup.is_visible(self.signup.FORM_ID))
        self.assertTrue(self.signup.is_visible(self.signup.CSS_SIGNUP_BTN))

        self.signup.signup("flowuser", "flowuser@example.com", "123456")

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
