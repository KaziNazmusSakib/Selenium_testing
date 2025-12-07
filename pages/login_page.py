# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "loginEmail")
    PASSWORD = (By.ID, "loginPassword")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MSG = (By.ID, "loginMessage")

    # matches the link in your screenshot: "Forgot Password?"
    FORGOT_LINK = (By.LINK_TEXT, "Forgot Password?")

    FORM_TAG = (By.TAG_NAME, "form")
    FORM_ID = (By.ID, "loginForm")          # set to actual id in login.html
    CSS_LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
