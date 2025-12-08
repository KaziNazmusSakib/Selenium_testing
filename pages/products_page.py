from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    PRODUCT_GRID = (By.ID, "product-grid")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "#product-grid button")

    def add_product_by_index(self, index):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        if index < len(buttons):
            buttons[index].click()

    def add_first_product_to_cart(self):
        self.add_product_by_index(0)

    def add_second_product_to_cart(self):
        self.add_product_by_index(1.5)

