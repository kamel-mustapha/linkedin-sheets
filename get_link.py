import time
from selenium import webdriver
from login import login

SELENIUM_LINK = "http://localhost:30000"
global_driver = None

def get_driver():
    global global_driver
    if global_driver is None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-dev-shm-usage')        
        global_driver = webdriver.Remote(
            command_executor=f'{SELENIUM_LINK}/wd/hub',
            options=chrome_options
        )
        login(global_driver)
        time.sleep(10)
    return global_driver

def get_sales_url(sales_link):
    driver = get_driver()
    try:
        driver.get(sales_link)
        time.sleep(10)
        return driver.current_url
    except Exception as e: print(e)
    finally: driver.quit()