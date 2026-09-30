"""
Get the current Euro to US Dollar exchange rate from the European Central Bank
"""

import requests
import json

def get_currency_exchange_rate():
    url = 'https://api.exchangeratesapi.io/latest?base=USD'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['rates']['EUR']

if __name__ == '__main__':
    print(get_currency_exchange_rate())