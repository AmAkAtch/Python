from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Rushiraj")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Gadhavi")

email_element = driver.find_element(By.NAME, value="email")
email_element.send_keys("trialid84@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value=".form-signin .btn")
submit.click()