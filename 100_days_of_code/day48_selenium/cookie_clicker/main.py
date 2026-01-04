from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import time


option = Options()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)

driver.get("https://ozh.github.io/cookieclicker/")
driver.implicitly_wait(3)

select_language = driver.find_element(By.ID, value="langSelect-EN")
if select_language:
    select_language.click()


def click_products():
    global check_store_time
    try:
        product_elements = driver.find_elements(By.CSS_SELECTOR, value=f".enabled")
        if len(product_elements)>2:
            best_upgrade = product_elements[-1]
            best_upgrade.click()
            check_store_time = time() + 5
    except:
        print("No upgrade available")

check_store_time = time()+5
while True:
    try:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
        if time()>check_store_time:
            click_products()
    except:
        print("Cookie confused me, trying again...")