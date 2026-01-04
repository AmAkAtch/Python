from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#CONSTANTs
USERNAME = "trial"
PASSWORD = "trial84"
EMAIL = "trialid84@gmail.com"

options=Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://appbrewery.github.io/gym/")

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


login_sequence()