import requests
from bs4 import BeautifulSoup

url = 'https://example.com/'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

headlines = []
for tag in soup.find_all('h1', class_='headline'):
    headline = tag.string
    headlines.append(headline)