from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    REMOVE_BTN = (By.XPATH, "//button[contains(text(),'Remove')]")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item(self):
        self.click(self.ADD_TO_CART_BTN)

    def remove_item(self):
        self.click(self.REMOVE_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)