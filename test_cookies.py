import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os.path import exists



driver = webdriver.Chrome()

driver.implicitly_wait(15)

USERNAME = "adpadillar"
PASSWORD = "soxroc-qubsi9-zyppuB"

def login():
    if exists("cookies.pkl"):
        driver.get("https://lichess.org/")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for c in cookies:
            print(c.get("domain"))
            driver.add_cookie(c)
        driver.refresh()
    else:
        driver.get("https://lichess.org/login")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_btn = driver.find_element(By.CSS_SELECTOR, ".submit")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_btn.click()
        time.sleep(10)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    
login()
time.sleep(5)






