import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from insta_follow_bot import InstaFollowBot


"""
Login not working
check follow button final peice of the code

"""


load_dotenv()

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

#initialize the selenium webdriver
options = Options()
options.add_argument("--disable-features=PasswordLeakDetection")
options.add_experimental_option("detach", True)
# Option: Disable the "Save Password" bubble as well (often helpful)
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)
is_login_success = False

#create object for insta_follow_bot
follow_bot = InstaFollowBot(driver)
is_login_success = follow_bot.insta_login()
if is_login_success:
    follow_bot.search_insta_account(SIMILAR_ACCOUNT)
    follow_bot.follow_people()
else:
    print(f"Login was not successfull")



