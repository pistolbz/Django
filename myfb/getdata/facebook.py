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

    def login(self, cookie):
        self.driver.get('https://facebook.com')
        self.cookie = 'Cookie: ' + cookie
        script = 'javascript:void(function(){ function setCookie(t) { var list = t.split("; "); console.log(list); for (var i = list.length - 1; i >= 0; i--) { var cname = list[i].split("=")[0]; var cvalue = list[i].split("=")[1]; var d = new Date(); d.setTime(d.getTime() + (7*24*60*60*1000)); var expires = ";domain=.facebook.com;expires="+ d.toUTCString(); document.cookie = cname + "=" + cvalue + "; " + expires; } } function hex2a(hex) { var str = ""; for (var i = 0; i < hex.length; i += 2) { var v = parseInt(hex.substr(i, 2), 16); if (v) str += String.fromCharCode(v); } return str; } setCookie("' + self.cookie + '"); location.href = "https://facebook.com"; })();'
        self.driver.execute_script(script)

    def get_posts_id_of_page(self, page_id):
        self.driver.get('https://mbasic.facebook.com/profile.php?id=' + page_id)
        posts_id = []
        while len(posts_id) < 100:
            print(len(posts_id))
            posts = self.driver.find_elements_by_tag_name('article')
            posts = [post.get_attribute('data-ft').split(',')[1].split(':')[1].replace('"','') for post in posts]
            posts_id.extend(posts)
            time.sleep(3)
            self.driver.find_element_by_partial_link_text("Hiển thị thêm").click()
        return posts_id

    def get_people_comment_of_post(self, page_id, post_id):
        self.driver.get('https://mbasic.facebook.com/story.php?story_fbid=' + post_id + '&id=' + page_id)
        people_comment = []
        while True:
            people = self.driver.find_elements_by_tag_name("h3")
            people = [str(person.text) + str("|") + str(person.find_element_by_tag_name("a").
            get_attribute("href")) for person in people]
            del people[0]
            people_comment.extend(people)
            print(len(people_comment))
            time.sleep(3)
            check_comment = self.driver.find_elements_by_partial_link_text("Xem thêm bình luận")
            if(check_comment):
                check_comment[0].click()
            else:
                break
        return people_comment
        

cookie = ''
page_id = ''
post_id = ''

facebook = UsingFacebookToGetData()
facebook.login(cookie)
time.sleep(5)

#posts_id = facebook.get_posts_id_of_page(page_id)
#for post_id in posts_id:
#    print(post_id)

people_comment = facebook.get_people_comment_of_post(page_id, post_id)
for person in people_comment:
    print(person)
