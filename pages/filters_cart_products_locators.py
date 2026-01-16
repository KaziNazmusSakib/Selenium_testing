from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class FiltersPage(BasePage):
    CATEGORY_FILTERS = (By.ID, "category-filters")
    CATEGORY_ITEMS = (By.CSS_SELECTOR, "#category-filters button")
    APPLY_FILTERS_BTN = (By.ID, "apply-filters-btn")
    CLEAR_FILTERS_BTN = (By.ID, "clear-filters-btn")

    def click_first_category(self):
        # wait until at least one category button exists
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.CATEGORY_ITEMS)
        )
        time.sleep(3)
        buttons = self.driver.find_elements(*self.CATEGORY_ITEMS)
        if buttons:
            buttons[0].click()

    def apply_filters(self):
        self.click(self.APPLY_FILTERS_BTN)

    def clear_filters(self):
        self.click(self.CLEAR_FILTERS_BTN)



class ProductsPage(BasePage):
    PRODUCT_GRID = (By.ID, "product-grid")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "#product-grid button")

    def add_product_by_index(self, index: int):
        # wait until product cards are rendered
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.ADD_TO_CART_BTNS)
        )
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        if index < len(buttons):
            buttons[index].click()

    def add_first_product_to_cart(self):
        self.add_product_by_index(0)

    def add_second_product_to_cart(self):
        self.add_product_by_index(1)


class CartPage(BasePage):
    CART = (By.ID, "cart")
    CART_ITEMS = (By.ID, "cart-items")
    TOTAL_PRICE = (By.ID, "total-price")
    CHECKOUT_BTN = (By.ID, "checkout-btn")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "#cart-items button")  # "Remove" buttons

    def get_items_text(self):
        element = self.driver.find_element(*self.CART_ITEMS)
        return element.text

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def remove_single_items(self):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        for btn in buttons:
            btn.click()
            time.sleep(2)
