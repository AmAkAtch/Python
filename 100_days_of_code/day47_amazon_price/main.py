import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_USER = os.getenv("EMAIL")
GMAIL_PASS = os.getenv("PASS")
LOWEST_PRICE = 1599
PRODUCT_NAME = "EvoFox One S"
def send_mail(price:float):
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASS)
        message_body = f"Price of {PRODUCT_NAME} has dropped below its lowest price you have set, Buy it right now at ${price}"
        connection.sendmail(from_addr=GMAIL_USER, to_addrs=GMAIL_USER, msg=f"Subject:Amazon Price Drop Alert!\n\n{message_body}")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
}

response = requests.get("https://www.amazon.in/gp/product/B0DZ6T16SD/ref=ewc_pr_img_1?smid=A2GTG1HPYW8M2P&th=1", headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price_element = soup.select_one("span.a-price span.a-offscreen")
current_price = float(price_element.getText().strip("₹").replace(",", ""))

if price_element:
    print(f"Full Price: {price_element.text}") 
    if current_price<LOWEST_PRICE:
        send_mail(current_price)

else:
    print("Price not found")