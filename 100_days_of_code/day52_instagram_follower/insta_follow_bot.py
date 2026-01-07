import os
import time
from dotenv import load_dotenv
from random import random
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
                login_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
                )
                print("Soft block detected. Waiting 5 seconds before retrying...")
                time.sleep(5) 
                self.driver.refresh() 
                continue
            except Exception as e:
                print("Proceeding to find error")
                break
        
        #reject the save password element that pops up
        try:
            save_password_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button" and contains(text(), "Not now")]')))
            save_password_element.click()
        except Exception as e:
            print(f"Save password dialogue did not appear: {e}")
        
        return True

    def search_insta_account(self, account_name):
        print("Searching sequence for Instagram account beginning...")        #find the search button using X path
        # search_icon = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[local-name()='svg' and @aria-label='Search']"))
        # )
        # search_icon.click()

        # try:
        #     print("Finding the search box and sending keys")
        #     search_box = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR,"input[aria-label='Search input']"))
        #         )
        #     search_box.send_keys(account_name)
        # except Exception as e:
        #     print(f"Error while trying to send keys {e}")
    
        # going directly to the url of the page to search the page
        self.driver.get(f"https://www.instagram.com/{account_name}")

    def follow_people(self):
        print("Starting sequence to follow people...")

        #open the followers
        print("Trying to find and click followers")
        all_followers = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
        )
        all_followers.click()


        #follow people by clicking on follow button    
        print("Trying to find the button with Xpath")
        follow_buttons = WebDriverWait(self.driver, 10).until(
          EC.presence_of_all_elements_located((
                By.XPATH, 
                "//button[.//div[text()='Follow']]"
            ))
        )
        print(f"Found {len(follow_buttons)} buttons. Starting follow loop...")
        for button in follow_buttons:
            try:
                # 1. Try the "Human" click first
                button.click()
                
            except Exception as e:
                # 2. If blocked by the "loading-state" overlay, use the "Nuclear Option"
                print("Click blocked by loading spinner. Forcing it with JS...")
                self.driver.execute_script("arguments[0].click();", button)

            except Exception as e:
                print(f"Click failed for other reason: {e}")

            # 3. CRITICAL: Wait for the 'loading-state' to disappear!
            # If you don't wait, the overlay will still be there for the next button.
            # Random sleep also helps avoid bot detection.
            sleep_time = random.uniform(2, 4)
            time.sleep(sleep_time)
