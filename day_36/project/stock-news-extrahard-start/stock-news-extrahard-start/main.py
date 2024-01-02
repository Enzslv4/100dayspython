from twilio.rest import Client
from datetime import datetime
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
day = datetime.now().day
news_title = ''
news_description = ''


#------------------------ STOCKS CONFIGS ------------------------#
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stocks_api_key = '45HA7TWQERTM4W8Y'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={stocks_api_key}'
r = requests.get(url)
data = r.json()

def defining_vars(d):
    if d < 10:
        starting_price = data['Time Series (Daily)'][f'2023-12-0{day - 1}']['1. open']
        final_price = data['Time Series (Daily)'][f'2023-12-0{day - 1}']['4. close']
    else:
        starting_price = data['Time Series (Daily)'][f'2023-12-{day - 1}']['1. open']
        final_price = data['Time Series (Daily)'][f'2023-12-{day - 1}']['4. close']
    v = float(final_price) / float(starting_price)
    return v

try:
    variation = defining_vars(day)
except KeyError:
    if day > 3:
        day = day - 3
    variation = defining_vars(day)


#------------------------ NEWS CONFIGS ------------------------#
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    

def get_news():
    global variation
    if variation >= 1.05:
        print('Get news.')
    elif variation <= .95:
        print('Get news.')
    else:
        print('Not enought variation')

news_api_key = 'e3ce7616685e472291bcfd626a7354d8'

url = ('https://newsapi.org/v2/everything?'
       f'q={STOCK}&'
       f'from=2023-12-{day}&'
       'sortBy=popularity&'
       f'apiKey={news_api_key}')

response = requests.get(url)
news_data = response.json()


#------------------------ TWILIO CONFIGS ------------------------#
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

account_sid = 'AC6d5202cc63d426e612d82efb949a22bd'
auth_token = 'f5afe5a8bdde29913fdc625391bd1782'
client = Client(account_sid, auth_token)

def send_sms(t):
    global news_data

    message = client.messages.create(
            from_='+14803861954',
            body=f'{t}',
            to='MY NUMB'      # Actually not working because of obvious reasons
        )
    
    print(message.status)


def text_form():
    try:
        news_title = news_data['articles'][0]['title']
        news_description = news_data['articles'][0]['description']
        text = f'Headline: {news_title}.\nBrief:{news_description}.'
    except KeyError:
        text = 'No news today!'
    return text

if variation > 1.05:
    body = text_form()
    t = f'TSLA: 🔺5%\n{body}'
    send_sms(t)
elif variation < .95:
    body = text_form()
    t = f'TSLA: 🔻5%\n{body}'
    send_sms(t)
