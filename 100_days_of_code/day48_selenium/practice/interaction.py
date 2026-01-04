from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_count_element.text)

driver.quit()