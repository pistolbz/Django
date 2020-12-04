from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re


class UsingFacebookToGetData:
    def __init__(self):
        CHROMEDRIVER_PATH = 'E:/chromedriver.exe'
        WINDOWS_SIZE = '1366,768'
        options = Options()
        #options.add_argument('--headless')
        options.add_argument('--windows-size=%s' % WINDOWS_SIZE)
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    def getdata(self):
        self.driver.get('https://mbasic.facebook.com/story.php?story_fbid=1552451458277937&id=740570182799406')
        posts = self.driver.find_element_by_class_name('cx eh ei')
        print(posts)

facebook = UsingFacebookToGetData()
facebook.getdata()
