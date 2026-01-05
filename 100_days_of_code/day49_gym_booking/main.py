from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

today = datetime.now()
day_today = today.strftime("%A")
print(day_today)

#CONSTANTs
USERNAME = "trial"
PASSWORD = "trial84"
EMAIL = "trialid84@gmail.com"

#information
classes_booked=0
waitlists_joined=0
already_booked_waitlisted=0
total_tuesday_6pm_classes_processed=0
total_thursday_6pm_classes_processed=0

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://appbrewery.github.io/gym/")

days_tobe_booked = ['tue', 'thu']

def login_sequence():
    try:
        login_button = driver.find_element(By.ID, value="login-button")
        if login_button: login_button.click()

        email_input = driver.find_element(By.ID, value="email-input")
        email_input.send_keys(EMAIL)

        pass_input = driver.find_element(By.ID, value="password-input")
        pass_input.send_keys(PASSWORD)

        submit_button = driver.find_element(By.ID, value="submit-button")
        submit_button.click()

        try:
            driver.find_element(By.ID, value="error-message")
        except e:
            print(f"No error in login: {e}")
        else:
            register_button = driver.find_element(By.ID, value="toggle-login-register")
            register_button.click()

            driver.find_element(By.ID, value="name-input").send_keys("Trial")

            driver.find_element(By.ID, value="submit-button").click()

    except Exception as e:
        print(f"Error occured while tring to execute the login sequence: {e}")
        print("Trying Again...")
        login_sequence()

def book_tuesday_class(day):
    global classes_booked, already_booked_waitlisted, waitlists_joined, total_tuesday_6pm_classes_processed, total_thursday_6pm_classes_processed
    print(f"Starting Booking process for {day}")
    tuesday_classes = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,f"div[id*='{day}']"))
    )    
    six_pm_class = tuesday_classes.find_element(By.CSS_SELECTOR, value="div[id*='-1800']")
    book_button = six_pm_class.find_element(By.TAG_NAME, value="button")
    if six_pm_class.get_attribute("data-user-booked")!="true":
        if book_button.text == "Join Waitlist":
            waitlists_joined+=1
            print(f"{day} waitlist Joined")
        else:
            classes_booked+=1
            print(f"{day} Class Joined")
        book_button.click()
    else:
        already_booked_waitlisted+=1
        print(f"{day} Class was already Booked/waitlisted")
    if day=="tue":
        total_tuesday_6pm_classes_processed+=1
    else:
        total_thursday_6pm_classes_processed+=1

login_sequence()
for day in days_tobe_booked:
    book_tuesday_class(day)
print(f"classes_booked: {classes_booked}\nwaitlists_joined: {waitlists_joined}\nalready_booked_waitlisted: {already_booked_waitlisted}\ntotal_tuesday_6pm_classes_processed: {total_tuesday_6pm_classes_processed}\ntotal_thursday_6pm_classes_processed: {total_thursday_6pm_classes_processed}")