"""
Create a code in Python to get the current stock price of a company from yahoo finance.

Input: ticker = "AAPL"
"""

import requests

def get_stock_price(ticker):
    url = 'https://finance.yahoo.com/quote/' + ticker
    response = requests.get(url)
    data = response.text.split('"regularMarketPrice":{"raw":')[1].split(',"fmt"')[0]
    return float(data)

print(get_stock_price('AAPL'))