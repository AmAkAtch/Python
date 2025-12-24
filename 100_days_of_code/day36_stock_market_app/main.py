import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "QMN5MB4TQ0DETYNO"
API_KEY_NEWS = "19ae5435e26b4485b8280e761ffc9aac"

date_today = datetime.now().date()
date_yesterday = str(date_today - timedelta(days=1))
date_day_before = str(date_today - timedelta(days=2))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_price_change():
    stock_data_parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey":API_KEY_STOCK,
    }

    stock_data = requests.get("https://www.alphavantage.co/query", params=stock_data_parameters).json()['Time Series (Daily)']

    close_yesterday = float(stock_data[date_yesterday]['4. close'])
    close_day_before = float(stock_data[date_day_before]['4. close'])

    price_change = ((-close_yesterday+close_day_before)/close_day_before)*100

    if price_change:
        get_news(price_change)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(price_change: float): 
    params_news_request = {
        "q":COMPANY_NAME,
        "from":date_day_before,
        "to":date_yesterday,
        "sortBy":"publishedAt",
        "pageSize":4,
        "apiKey":API_KEY_NEWS,
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=params_news_request).json()['articles']
    if news_response:
        send_alert(price_change, news_response)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_alert(price_change: float, news_response: list):
    print(f'{STOCK}: {round(price_change,2)}')
    for news in news_response:
        print("--------------------")
        print(f'Headline: {news['title']}')
        print(f'Brief: {news['description']}')


get_stock_price_change()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

