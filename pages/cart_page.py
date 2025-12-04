from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CART = (By.ID, "cart")
    CART_ITEMS = (By.ID, "cart-items")
    TOTAL_PRICE = (By.ID, "total-price")
    CHECKOUT_BTN = (By.ID, "checkout-btn")

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def get_items_text(self):
        return self.get_text(self.CART_ITEMS)
