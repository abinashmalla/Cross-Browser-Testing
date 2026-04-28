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
def test_workflow(browser):
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

    assert "inventory" in driver.current_url

    time.sleep(4)
    cartBtn=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    cartBtn.click()
    time.sleep(1)
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
    time.sleep(1)
    print("Add to Card 3")
    cartBtn4=driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
    cartBtn4.click()
    time.sleep(1)
    print("Remove to Card 3")

    driver.switch_to.window(driver.current_window_handle)

    Back_To_products = wait1.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    Back_To_products.click()
    print("Back to product")



    select_Box=driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
    select_Box.click()
    time.sleep(1)
    driver.find_element(By.XPATH,"(//option[@value='lohi'])[1]").click()
    time.sleep(1)


    dropdown = wait1.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']")))
    dropdown.click()
    time.sleep(1)

    button = wait1.until(EC.visibility_of_element_located((By.ID, "checkout")))
    button.click()
    time.sleep(2)

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
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,500);")


    continueBtn = driver.find_element(By.NAME, "continue")
    time.sleep(1)
    continueBtn.click()
    print("Click Continue")

    time.sleep(1)
    driver.execute_script("window.scrollBy(0,500);")
    finishBtn = driver.find_element(By.NAME, "finish")
    time.sleep(1)
    finishBtn.click()
    print("Click Finish")

    driver.execute_script("window.scrollBy(500,0);")
    time.sleep(3)
    Back_Home=driver.find_element(By.XPATH,"//button[@id='back-to-products']")
    Back_Home.click()
    print("Back to Home")
    time.sleep(1)

    # try:
    #     scroll_container = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "#react-burger-menu-btn"))
    #     )
    #
    #     # Scroll to the far right first
    #     driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scroll_container)
    #     time.sleep(1)  # Pause to see the effect
    #
    #     # Now scroll from right to left smoothly
    #     for x in range(scroll_container.scrollWidth, -1, -50):  # step -50 px
    #         driver.execute_script(f"arguments[0].scrollLeft = {x}", scroll_container)
    #         time.sleep(0.02)  # Smooth scrolling effect
    #
    #     time.sleep(2)
    #
    # finally:
    #     pass

    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    print("Logout page")


    time.sleep(3)
    driver.quit()