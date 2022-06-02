from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME, "q")
driver.implicitly_wait(4)
searchInput.send_keys("python")
searchInput.send_keys(Keys.ENTER)
searchElements = driver.find_elements(By.CSS_SELECTOR, ".repo-list-item .f4 a")
for element in searchElements:
    print(element.text)
#result = driver.page_source #buradan kaynak kodlara ulaşıp bs4 ile de işlem yapılabilir.
driver.close()
