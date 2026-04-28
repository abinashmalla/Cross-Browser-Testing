import sys

import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.mark.parametrize("browser", ["chrome", "firefox","ChromiumEdge"])
def test_login(browser):
    driver = get_driver(browser)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()

    wait1 = WebDriverWait(driver, 5)
    driver.maximize_window()

    try:
        if "product" in driver.page_source:
            print("Login successful!")
            assert True
        else:
            raise AssertionError("Login failed - 'product' not found in page source.")

    except Exception as e:
        print(f"Error! {str(e)}")
        assert False
    time.sleep(5)
    add_To_Cart = wait1.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")))
    add_To_Cart.click()
    print("Add to Card")
    time.sleep(1)

    Back_To_products = wait1.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    Back_To_products.click()
    print("Back to product")
    time.sleep(2)

    dropdown = wait1.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']")))
    dropdown.click()
    time.sleep(2)

    button = wait1.until(EC.visibility_of_element_located((By.ID, "checkout")))
    button.click()
    time.sleep(4)

    driver.find_element(By.CLASS_NAME, "checkout_info")
    print("Fill the form")

    firstName = driver.find_element(By.NAME, "firstName")
    firstName.send_keys("abinash")
    time.sleep(1)
    lastName = driver.find_element(By.NAME, "lastName")
    lastName.send_keys("malla")
    time.sleep(1)
    postalCode = driver.find_element(By.ID, "postal-code")
    postalCode.send_keys("44600")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,500);")
    time.sleep(2)

    continueBtn = driver.find_element(By.NAME, "continue")
    time.sleep(1)
    continueBtn.click()
    print("Click Continue")

    time.sleep(2)
    finishBtn = driver.find_element(By.NAME, "finish")
    time.sleep(2)
    finishBtn.click()
    print("Click Finish")
    driver.execute_script("window.scrollBy(500,0);")

    time.sleep(3)
    driver.quit()