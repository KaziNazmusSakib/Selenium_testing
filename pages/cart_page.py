# in CartPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART = (By.ID, "cart")
    CART_ITEMS = (By.ID, "cart-items")
    TOTAL_PRICE = (By.ID, "total-price")
    CHECKOUT_BTN = (By.ID, "checkout-btn")

    def get_items_text(self):
        element = self.driver.find_element(*self.CART_ITEMS)
        return element.text

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_item(self):
        # adjust selector to your "Remove" buttons in the cart
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "#cart button.remove")
        if buttons:
            buttons[0].click()
