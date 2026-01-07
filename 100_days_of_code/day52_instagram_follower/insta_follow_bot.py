import os
import time
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
        MAX_RETRIES = 3
        for attempt in range(1, MAX_RETRIES+1):

            print(f"Login Attempt {attempt} of {MAX_RETRIES}...")
            self.driver.get("https://instagram.com")
            
            username_input = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username'], input[type='text']")))
            username_input.send_keys(self.USER_NAME)

            password_input = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"], input[name="pass"]')))
            password_input.send_keys(self.PASSWORD, Keys.ENTER)

            try:
                error_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'There was a problem logging you into Instagram')]"))
                )
                
                print("Soft block detected. Waiting 10 seconds before retrying...")
                time.sleep(10) 
                self.driver.refresh() 
                continue 
                
            except Exception as e:
                print("No error message found. Assuming success (or captcha).")
                break 
        try:
            save_password_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button" and contains(text(), "Not now")]')))
            save_password_element.click()
        except Exception as e:
            print(f"Save password dialogue did not appear: {e}")

    def search_insta_account(self, account_name):
        print("Trying Search")
        time.sleep(5)
        # try:
        #     search_icon = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Search']/.."))
        #     )
        #     search_icon.click()
        # except Exception as e:
        #     print(f"Exception in CSS tags: {e}")

        try:
            print("trying x path")
            search_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[local-name()='svg' and @aria-label='Search']"))
            )
            search_icon.click()
        except Exception as e:
            print(f"Exception in x path: {e}")
        else:
            text_input = 