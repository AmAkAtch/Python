from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

PRODUCT_URL = "https://www.amazon.in/gp/product/B0FC284LX2/ref=ox_sc_act_title_1?smid=A2GTG1HPYW8M2P&th=1"

#Add experimental Option detach to True to keep the window open even after the file completes the execution
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(PRODUCT_URL)

price_element = driver.find_element(By.CLASS_NAME,"a-offscreen").get_attribute("textContent")
print(price_element)

driver.quit()