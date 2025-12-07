from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):
    USERNAME = (By.ID, "signupUser")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    SIGNUP_BTN = (By.XPATH, "//button[@type='submit']")

    FORM_TAG = (By.TAG_NAME, "form")
    FORM_ID = (By.ID, "signupForm")         # matches signup.html
    CSS_SIGNUP_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def signup(self, username, email, password):
        self.type(self.USERNAME, username)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SIGNUP_BTN)
