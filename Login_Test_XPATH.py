from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

username = "visual_user"
password = "secret_sauce"


def testby_xpath(browser, username, password):
    browser.get("https://www.saucedemo.com/")

    # Relative XPATH found by 2 attributes
    usernameField = browser.find_element(By.XPATH, "//*[@id='user-name']")
    usernameField.send_keys(username)

    # Relative XPATH found for searching by any keyword
    passwordField = browser.find_element(By.XPATH, "//*[@id='password']")
    passwordField.send_keys(password)

    # Relative XPATH found for searching by partial match
    submitButton = browser.find_element(By.XPATH, "//*[contains(@name,'login-')]")
    submitButton.click()


testby_xpath(browser, username, password)

time.sleep(8)
browser.quit()
