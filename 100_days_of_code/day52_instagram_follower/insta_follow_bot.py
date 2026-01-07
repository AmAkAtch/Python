import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class InstaFollowBot:
    #load environment variables
    load_dotenv()

    #get userdata from env for instagram
    USER_NAME = os.environ["INSTA_USER"]
    PASSWORD = os.environ["PASSWORD"]

    def __init__(self, driver):
        self.driver = driver
    
    def insta_login(self):
        self.driver.get("https://instagram.com")
        
        username_input = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(1) > div > label > input")))
        username_input.send_keys(self.USER_NAME)

        password_input = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(2) > div > label > input")))
        password_input.send_keys(self.PASSWORD, Keys.ENTER)

        try:
            save_password_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button" and contains(text(), "Not now")]')))
            save_password_element.click()
        except Exception as e:
            print(f"Save password dialogue did not appear: {e}")