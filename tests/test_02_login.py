# tests/test_02_login.py
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


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

        self.login = LoginPage(self.driver)
        self.signup = SignupPage(self.driver)
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)

    def test_login_locators_and_flow(self):
        self.driver.get("F:/Selenium_testing/auth/login.html")

        self.assertTrue(self.login.is_visible(self.login.EMAIL))
        self.assertTrue(self.login.is_visible(self.login.PASSWORD))
        self.assertTrue(self.login.is_visible(self.login.LOGIN_BTN))
        self.assertTrue(self.login.is_visible(self.login.FORGOT_LINK))
        self.assertTrue(self.login.is_visible(self.login.FORM_TAG))
        self.assertTrue(self.login.is_visible(self.login.FORM_ID))
        self.assertTrue(self.login.is_visible(self.login.CSS_LOGIN_BTN))

        self.login.login("flowuser@example.com", "123456")

        # handle "No user found" alert (same logic you had)
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            if "No user found" in text:
                alert.accept()
                self.driver.get("F:/Selenium_testing/auth/sign-up.html")
                self.signup.signup("flowuser", "flowuser@example.com", "123456")
                time.sleep(1)
                self.driver.get("F:/Selenium_testing/auth/login.html")
                self.login.login("flowuser@example.com", "123456")
        except Exception:
            pass

        time.sleep(1)
        # self.assertIn("index.html", self.driver.current_url)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
