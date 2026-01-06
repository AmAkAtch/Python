import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from insta_follow_bot import InstaFollowBot

#load environment variables
load_dotenv()

#get userdata from env for instagram
USER_NAME = os.environ["INSTA_USER"]
PASSWORD = os.environ["PASSWORD"]

#initialize the selenium webdriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#create object for insta_follow_bot
follow_bot = InstaFollowBot(driver)



