from instagram_UserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


class Instagram():
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages' : 'en,en_US'})
        serv = Service('chromedriver.exe')
        self.browser = webdriver.Chrome(service=serv,options=self.browserProfile)
        self.username = username
        self.password = password
        self.followers = []

    def login(self):
        self.browser.get("https://www.instagram.com")
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

    def getFollowers(self):
        self.browser.implicitly_wait(3)
        self.browser.find_element(By.XPATH,
                                  '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span').click()
        self.browser.find_element(By.XPATH,
                                  '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
        total_count = int(self.browser.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').text)
        self.browser.find_element(By.XPATH,
                                  '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
        action = webdriver.ActionChains(self.browser)
        print(total_count)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            counter = len(dialog.find_elements(By.CSS_SELECTOR, 'li'))
            time.sleep(0.5)
            if counter == total_count - 1 or counter == total_count:
                break
            else:
                continue
        followers = dialog.find_elements(By.CSS_SELECTOR, 'li')
        for user in followers:
            self.followers.append(user.find_element(By.CSS_SELECTOR, "a").get_attribute("href"))
        with open("followers.txt","w",encoding="utf-8") as file:
            for i in self.followers:
                file.write(i+"\n")
    def followSomeone(self):
        following = input("Who do you want to follow:")
        self.browser.get("https://www.instagram.com/"+following)
        self.browser.implicitly_wait(3)
        follow_button = self.browser.find_element(By.TAG_NAME,'button')
        if follow_button.text == "Follow":
            follow_button.click()
            time.sleep()
        else:
            print(f"You already followed {following}")
    def unfollowSomeone(self):
        unfollowing = input("Who do you want to unfollow:")
        self.browser.get("https://www.instagram.com/" + unfollowing)
        unfollowing_button = self.browser.find_element(By.XPATH,'.//span[@aria-label="Following"]')
        unfollowing_button.click()
        self.browser.find_element(By.XPATH,'//button[text()="Unfollow"]').click()
instagram = Instagram(username, password)
instagram.login()
instagram.unfollowSomeone()
