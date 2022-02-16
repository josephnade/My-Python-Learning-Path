import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from twitterUserInfo import username,password
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self,username,password):
        self.driverProfile = webdriver.ChromeOptions()
        self.driverProfile.add_experimental_option('prefs',{'intl.accept_languages' : 'en,en_US'})
        serv = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv,options=self.driverProfile)
        self.username = username
        self.password = password
        self.tweets = []
    def login(self):
        self.driver.get("https://twitter.com/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'.//a[@href="/login"]').click()
        self.driver.find_element(By.XPATH,'.//input[@type="text"]').send_keys(self.username)
        self.driver.find_element(By.XPATH,'//*[contains(text(),"Next")]').click()
        self.driver.find_element(By.XPATH,'.//input[@type="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH,'//*[contains(text(),"Log in")]').click()
    def search_hashtag(self,hashtag,how_many_tweet):
        self.driver.implicitly_wait(5)
        search_input = self.driver.find_element(By.XPATH,'.//input[@placeholder = "Search Twitter"]')
        search_input.send_keys(hashtag)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1.5)
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight;")
        counter = 0
        while True:
            self.driver.execute_script('return window.scrollTo(0,document.documentElement.scrollHeight);')
            time.sleep(1.5)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight;")
            if last_height == new_height:
                break
            last_height = new_height
            tweet = self.driver.find_elements(By.XPATH,'.//article[@data-testid="tweet"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
            if len(self.tweets) > how_many_tweet:
                break
            for e in tweet:
                self.tweets.append(e.text)
                counter+=1
                print(f"{counter}. tweet: {e.text}\n***************\n")
        with open("twitter.txt","w",encoding="utf-8") as file:
            for item in self.tweets:
                file.write(item+"\n")

twitter =Twitter(username,password)
twitter.login()
how_many_tweet = int(input("How many tweet do you want to see:"))
twitter.search_hashtag("python",how_many_tweet)

