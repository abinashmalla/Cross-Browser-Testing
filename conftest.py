import pytest
from selenium import webdriver
from  selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def browser():
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # driver = webdriver.ChromiumEdge()


    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()