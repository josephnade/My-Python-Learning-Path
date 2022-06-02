from github_UserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]').click()

    def Repos(self):
        self.signIn()
        self.browser.implicitly_wait(3)
        repos = self.browser.find_elements(By.CSS_SELECTOR, ".list-style-none .public a")
        for element in repos:
            print(element.text)
        self.browser.close()


github = Github(username, password)
github.Repos()
