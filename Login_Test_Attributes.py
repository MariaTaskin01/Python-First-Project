from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

username = "visual_user"
password = "secret_sauce"

def test_fields(browser, username, password):

    browser.get("https://www.saucedemo.com/")

    usernameField = browser.find_element(By.CLASS_NAME, "input_error.form_input")
    usernameField.send_keys(username)

    passwordField = browser.find_element(By.NAME, "password")
    passwordField.send_keys(password)

    submitButton = browser.find_element(By.ID,"login-button")
    submitButton.click()

test_fields(browser, username, password)

time.sleep(10)

browser.quit()






