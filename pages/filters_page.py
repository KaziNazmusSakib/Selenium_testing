from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FiltersPage(BasePage):
    
    CATEGORY_FILTERS = (By.ID, "category-filters")
    APPLY_BTN = (By.ID, "apply-filters-btn")
    CLEAR_BTN = (By.ID, "clear-filters-btn")

    def apply_filters(self):
        self.click(self.APPLY_BTN)

    def clear_filters(self):
        self.click(self.CLEAR_BTN)
