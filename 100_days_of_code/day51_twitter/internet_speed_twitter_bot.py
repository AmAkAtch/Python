from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.driver=driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")

        try:
            accept_trust = WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            sleep(3)
            accept_trust.click()
        except Exception as e:
            print(f"Trust button did not appear: {e}")

        go_button = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,"start-text")))
        go_button.click()

        try:
            result_data = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.result-data > a")))
        except Exception as e:
            print(f"Error while trying to look for resultdata: {e}")
        else: 
            up_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "upload-speed")))
            self.up = up_element.text
            print(f"Upload Speed: {self.up}")
            down_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "download-speed")))
            self.down = down_element.text
            print(f"Download Speed: {self.down}")

        try:
            close_popup = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.desktop-app-prompt-modal > div > a")))      
            close_popup.click()
        except Exception as e:
            print(f"Windows add did not come: {e}")

    def get_up_speed(self):
        return self.up
    
    def get_down_speed(self):
        return self.down

    def complain_on_twitter(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://x.com/i/flow/login")
        input_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "text")))
        input_box.send_keys("id_trial", Keys.ENTER)