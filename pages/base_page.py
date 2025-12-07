from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def type(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def click(self, locator):
        elem = self.find(locator)
        elem.click()

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def get_text(self, locator):
        return self.find(locator).text
