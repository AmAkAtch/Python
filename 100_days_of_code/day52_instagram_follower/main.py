from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from insta_follow_bot import InstaFollowBot


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

#create object for insta_follow_bot
follow_bot = InstaFollowBot(driver)
follow_bot.insta_login()



