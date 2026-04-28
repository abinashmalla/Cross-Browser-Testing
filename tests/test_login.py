import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
import time
@pytest.mark.parametrize("browser", ["chrome", "firefox","ChromiumEdge"])
def test_login(browser):
    driver = get_driver(browser)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url
    time.sleep(2)
    driver.quit()