# in ProductsPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    PRODUCT_GRID = (By.ID, "product-grid")

    def add_first_product_to_cart(self):
        # adjust selector to your "Add to Cart" buttons
        button = self.driver.find_element(By.CSS_SELECTOR, "#product-grid button")
        button.click()
