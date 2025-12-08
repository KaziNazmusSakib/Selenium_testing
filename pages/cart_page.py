# in CartPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    CART = (By.ID, "cart")
    CART_ITEMS = (By.ID, "cart-items")
    TOTAL_PRICE = (By.ID, "total-price")
    CHECKOUT_BTN = (By.ID, "checkout-btn")
    REMOVE_BUTTONS = (By.CLASS_NAME, "remove-from-cart")

    def get_items_text(self):
        element = self.driver.find_element(*self.CART_ITEMS)
        return element.text

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_multiple_items(self, how_many=2):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        for btn in buttons[:how_many]:
            btn.click()
            time.sleep(0.5)

