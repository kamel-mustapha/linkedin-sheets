import time, os, json
from selenium.webdriver.common.by import By

def fill_input(input, text, delay=0.5):
    for letter in text:
        input.send_keys(letter)
        time.sleep(delay)

def login(driver):
    CREDS = None
    with open("./linkedin-creds.json", "r") as f:
        CREDS = json.load(f)
    if not CREDS: return
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    username = driver.find_element(by=By.ID, value="username")
    password = driver.find_element(by=By.ID, value="password")
    login_form = driver.find_element(by=By.CLASS_NAME, value="login__form")
    fill_input(username, CREDS.get("username"))
    fill_input(password, CREDS.get("password"))
    time.sleep(2)
    login_form.submit()
    time.sleep(5)