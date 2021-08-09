''' Veja mais em www.lcsvillela.github.io/publicando-tweet-com-python.html
www.instagram.com/lcsvillela
www.twitter.com/lcsvillela
www.github.com/lcsvillela '''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from sys import argv


class TwitterBot():
    def __init__(self, username, password,
                 text="Fui automatizado! Confira: www.github.io/publicando-tweet-com-python.html"):
        self.__username = username
        self.__password = password
        self.__location = {'username': 'session[username_or_email]',
                           'password': 'session[password]',
                           'button_login': '//form/div/div[3]',
                           'button_tweet': "//*[@data-testid='tweetButtonInline']"}
        self.__driver = webdriver.Firefox()
        self.__text = text
        self.__wait = WebDriverWait(self.__driver, 30)
        self.__actions = ActionChains(self.__driver)
        self.start()

    def login_twitter(self):
        self.__driver.get("https://twitter.com/login")
        self.__wait.until(EC.presence_of_element_located((By.NAME, self.__location['username'])))
        self.__wait.until(EC.presence_of_element_located((By.NAME, self.__location['password'])))
        field_user = self.__driver.find_element_by_name(self.__location['username'])
        field_user.send_keys(self.__username)
        field_pass = self.__driver.find_element_by_name(self.__location['password'])
        field_pass.send_keys(self.__password)
        self.__driver.find_element_by_xpath('//form/div/div[3]').click()

    def make_tweet(self):
        self.__actions = ActionChains(self.__driver)
        self.__wait.until(EC.presence_of_element_located((By.XPATH, self.__location['button_tweet'])))
        ID = self.get_field_text()
        self.__wait.until(EC.element_to_be_clickable((By.ID, ID)))
        field_text = self.__driver.find_element_by_id(ID)
        self.__actions.move_to_element(field_text).click(field_text).send_keys(self.__text).perform()
        self.__driver.find_element_by_xpath(self.__location['button_tweet']).click()

    def get_field_text(self):
        code = self.__driver.page_source.split('"')
        return [x for x in code if 'placeholder-' in x][0]
