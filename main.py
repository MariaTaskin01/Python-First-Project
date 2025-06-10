import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Launch Browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Open Google
driver.get("https://www.google.com/")
time.sleep(2)

#Print title
print(driver.title)

#Close Browser
driver.quit()