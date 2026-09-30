import requests
from bs4 import BeautifulSoup

website = requests.get('https://www.amazon.com/Apple-iPhone-12-Unlocked-128GB/dp/B08HeG719F/ref=sr_1_1')
soup = BeautifulSoup(website.content, 'html.parser')

price_divs = []
price_divs = soup.find_all('span', {'class': 'a-price-whole'})

for price_div in price_divs:
    print(price_div.text)