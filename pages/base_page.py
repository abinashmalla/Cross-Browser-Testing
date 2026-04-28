from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def click(self, locator):
        element = self.find(locator)
        try:
            element.click()
        except Exception as e:
            raise Exception(f"Unable to click element {locator}: {str(e)}")

    def send_keys(self, locator, value):
        if value is None:
            raise ValueError("Input value cannot be None")
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find(locator).text