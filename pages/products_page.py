from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    PRODUCT_GRID = (By.ID, "product-grid")

    def grid_text(self):
        return self.get_text(self.PRODUCT_GRID)
