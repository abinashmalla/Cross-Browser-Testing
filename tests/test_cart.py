import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    wait1 = WebDriverWait(driver, 5)


    try:
        if "product" in driver.page_source:
            print("Login successful!")
            assert True
        else:
            raise AssertionError("Login failed - 'product' not found in page source.")

    except Exception as e:
        print(f"Error! {str(e)}")
        assert False
    time.sleep(4)
    cartBtn=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    cartBtn.click()
    time.sleep(2)
    cart_btn=driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']")
    cart_btn.click()
    driver.switch_to.window(driver.current_window_handle)

    wait1.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(2)
    wait1.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#remove-sauce-labs-bike-light"))).click()

    driver.switch_to.window(driver.current_window_handle)

    add_To_Cart = wait1.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")))
    time.sleep(1)
    add_To_Cart.click()
    time.sleep(1)
    print("Add to Card")
    cartBtn3=driver.find_element(By.XPATH, "//button[@id='add-to-cart']")
    cartBtn3.click()
    time.sleep(2)
    print("Add to Card 3")
    cartBtn4=driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
    cartBtn4.click()
    time.sleep(2)
    print("Remove to Card 3")

    driver.switch_to.window(driver.current_window_handle)

    Back_To_products = wait1.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    Back_To_products.click()
    print("Back to product")

    time.sleep(3)
    assert "inventory" in driver.current_url

    time.sleep(3)
    driver.quit()