from selenium import webdriver

driver = webdriver.Chrome()
url = "https://github.com"
driver.get(url)
driver.implicitly_wait(2)
driver.maximize_window()
driver.save_screenshot("github_homepage.png")
url = "https://github.com/josephnade"
driver.get(url)
print(driver.title)
driver.implicitly_wait(2)
if "josephnade" in driver.title:
    driver.save_screenshot("github_josephnade.png")
driver.back()
driver.implicitly_wait(2)
driver.close()