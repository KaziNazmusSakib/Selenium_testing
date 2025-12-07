from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FiltersPage(BasePage):
    CATEGORY_FILTERS = (By.ID, "category-filters")
    APPLY_FILTERS_BTN = (By.ID, "apply-filters-btn")
    CLEAR_FILTERS_BTN = (By.ID, "clear-filters-btn")

    def click_any_category(self):
        # wait 3 seconds before clicking the first category button
        import time
        time.sleep(3)
        btn = self.driver.find_element(By.CSS_SELECTOR, "#category-filters button")
        btn.click()

    def apply_filters(self):
        self.click(self.APPLY_FILTERS_BTN)

    def clear_filters(self):
        self.click(self.CLEAR_FILTERS_BTN)


class ProductsPage(BasePage):
    PRODUCT_GRID = (By.ID, "product-grid")

    def add_first_product_to_cart(self):
        # adjust selector to your "Add to Cart" buttons inside product-grid
        btn = self.driver.find_element(By.CSS_SELECTOR, "#product-grid button")
        btn.click()

class CartPage(BasePage):
    CART = (By.ID, "cart")
    CART_ITEMS = (By.ID, "cart-items")
    TOTAL_PRICE = (By.ID, "total-price")
    CHECKOUT_BTN = (By.ID, "checkout-btn")

    def get_items_text(self):
        # direct find; no visibility wait
        element = self.driver.find_element(*self.CART_ITEMS)
        return element.text

    def checkout(self):
        self.click(self.CHECKOUT_BTN)
