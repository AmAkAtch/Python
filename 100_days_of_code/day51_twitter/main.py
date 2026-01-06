from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot

load_dotenv()

options = Options()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)

internet_speed_bot = InternetSpeedTwitterBot(driver)

internet_speed_bot.get_internet_speed()
download_speed = internet_speed_bot.get_down_speed()
upload_speed = internet_speed_bot.get_up_speed()

if float(download_speed) < 150 and float(upload_speed) < 10:
    print("Complain on twitter")
# internet_speed_bot.complain_on_twitter()
