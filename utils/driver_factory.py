from selenium import webdriver

def get_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "ChromiumEdge":
        return webdriver.ChromiumEdge()
    elif browser == "safari":
        return webdriver.Safari()
    else:
        raise Exception("Unsupported browser")

