import requests
from bs4 import BeautifulSoup

url = 'url_of_webpage'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.find_all(text=True)

for t in text:
 print(t)