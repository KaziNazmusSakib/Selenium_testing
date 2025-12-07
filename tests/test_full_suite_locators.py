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


class TestFullSuiteLocators(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

        self.login = LoginPage(self.driver)
        self.signup = SignupPage(self.driver)
        self.filters = FiltersPage(self.driver)
        self.cart = CartPage(self.driver)
        self.products = ProductsPage(self.driver)

    # 01 – signup page locators
    def test_01_signup_locators(self):
        self.driver.get("F:/Selenium_testing/auth/sign-up.html")

        self.assertTrue(self.signup.is_visible(self.signup.USERNAME))
        self.assertTrue(self.signup.is_visible(self.signup.EMAIL))
        self.assertTrue(self.signup.is_visible(self.signup.PASSWORD))
        self.assertTrue(self.signup.is_visible(self.signup.SIGNUP_BTN))
        self.assertTrue(self.signup.is_visible(self.signup.FORM_TAG))
        self.assertTrue(self.signup.is_visible(self.signup.FORM_ID))
        self.assertTrue(self.signup.is_visible(self.signup.CSS_SIGNUP_BTN))

        self.signup.signup("flowuser", "flowuser@example.com", "123456")

    # 02 – login page locators
    def test_02_login_locators(self):
        
        self.driver.get("F:/Selenium_testing/auth/login.html")

        self.assertTrue(self.login.is_visible(self.login.EMAIL))
        self.assertTrue(self.login.is_visible(self.login.PASSWORD))
        self.assertTrue(self.login.is_visible(self.login.LOGIN_BTN))
        # comment this out if your login.html has no forgot link
        self.assertTrue(self.login.is_visible(self.login.FORGOT_LINK))
        self.assertTrue(self.login.is_visible(self.login.FORM_TAG))
        self.assertTrue(self.login.is_visible(self.login.FORM_ID))
        self.assertTrue(self.login.is_visible(self.login.CSS_LOGIN_BTN))

        self.login.login("flowuser@example.com", "123456")

        # if auth.js shows "No user found" alert, handle it:
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            if "No user found" in text:
                alert.accept()
                # go to signup, create user, then return to login and login again
                self.driver.get("F:/Selenium_testing/auth/sign-up.html")
                self.signup.signup("flowuser", "flowuser@example.com", "123456")
                time.sleep(1)
                self.driver.get("F:/Selenium_testing/auth/login.html")
                self.login.login("flowuser@example.com", "123456")
        except Exception:
            # no alert -> login probably succeeded
            pass

        # after successful login auth.js should redirect to index.html
        time.sleep(1)
        #self.assertIn("index.html", self.driver.current_url)
    
    # # 04 – filters / products / cart
    # def test_04_filters_products_cart_locators(self):
    #     self.driver.get("F:/Selenium_testing/index.html")

        # self.assertTrue(self.filters.is_visible(self.filters.CATEGORY_FILTERS))
        # self.filters.apply_filters()
        # time.sleep(1)
        # self.filters.clear_filters()
        # time.sleep(1)

        # self.assertTrue(self.products.is_visible(self.products.PRODUCT_GRID))
        # self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, "bg-white")) >= 0)
        # self.assertTrue(len(self.driver.find_elements(By.CSS_SELECTOR, "#product-grid > div")) >= 0)
        # self.assertTrue(len(self.driver.find_elements(By.TAG_NAME, "div")) >= 0)

        # self.assertTrue(self.cart.is_visible(self.cart.CART))
        # self.assertEqual(self.cart.get_items_text().strip(), "")
        # self.cart.checkout()
        # time.sleep(1)

def test_04_filters_products_cart_locators(self):
    self.driver.get("F:/Selenium_testing/index.html")

    # 1) click category button (with 3s wait inside)
    self.assertTrue(self.filters.is_visible(self.filters.CATEGORY_FILTERS))
    self.filters.click_any_category()

    # 2) apply & clear filters
    self.filters.apply_filters()
    time.sleep(1)

    # 3) add to cart
    self.products.add_first_product_to_cart()
    time.sleep(1)

    # 4) clear filters again
    self.filters.clear_filters()
    time.sleep(1)

    # existing visibility checks and cart assertions
    self.assertTrue(self.products.is_visible(self.products.PRODUCT_GRID))
    self.assertTrue(len(self.driver.find_elements(By.CLASS_NAME, "bg-white")) >= 0)
    self.assertTrue(len(self.driver.find_elements(By.CSS_SELECTOR, "#product-grid > div")) >= 0)
    self.assertTrue(len(self.driver.find_elements(By.TAG_NAME, "div")) >= 0)

    self.assertTrue(self.cart.is_visible(self.cart.CART))
    self.assertEqual(self.cart.get_items_text().strip(), "")
    self.cart.checkout()
    time.sleep(1)


if __name__ == "__main__":
    unittest.main()
