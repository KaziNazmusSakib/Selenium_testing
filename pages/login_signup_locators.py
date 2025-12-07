import unittest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        time.sleep(1)

    # -------------------------
    # SIGNUP TESTS
    # -------------------------
    def test_signup_success(self):
        self.driver.get("F:/Selenium_testing/auth/sign-up.html")
        signup = SignupPage(self.driver)
        signup.signup("sakib", "sakib@gmail.com", "123456")
        time.sleep(1)
        # Example assertion, depends on your page
        # self.assertIn("success", signup.get_message().lower())

    def test_signup_empty_fields(self):
        self.driver.get("F:/Selenium_testing/auth/sign-up.html")
        signup = SignupPage(self.driver)
        signup.signup("", "", "")
        time.sleep(1)
        # self.assertIn("required", signup.get_message().lower())

    # -------------------------
    # LOGIN TESTS
    # -------------------------
    def test_login_success(self):
        self.driver.get("F:/Selenium_testing/auth/login.html")
        login = LoginPage(self.driver)
        login.login("sakib@gmail.com", "123456")
        time.sleep(1)
        # self.assertIn("success", login.get_message().lower())

    def test_login_invalid_credentials(self):
        self.driver.get("F:/Selenium_testing/auth/login.html")
        login = LoginPage(self.driver)
        login.login("Akib@example.com", "wrongpass")
        time.sleep(1)
        # self.assertIn("invalid", login.get_message().lower())

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
