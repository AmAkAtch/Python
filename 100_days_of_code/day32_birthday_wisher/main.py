import pandas as pd
import random
from datetime import datetime
import smtplib

MY_EMAIL = "gadhavirushiraj7@gmail.com"


#import birthdays.csv
df_birthdays = pd.read_csv("day32_birthday_wisher/birthdays.csv")

now = datetime.now()
date_today = now.day
month_today = now.month

birthday_list = [item.to_dict() for _,item in df_birthdays.iterrows() if item["day"] == date_today and item["month"] == month_today ]

if birthday_list:
    for item in birthday_list:
        with open(f"day32_birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            message = letter.read()
            message = message.replace("[NAME]", item["name"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=item["email"], msg=f"Subject:Happy Birthday!!!\n\n{message}")
            