import requests
from bs4 import BeautifulSoup

url = "https://www.example.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# extract information from HTML
data = soup.find_all("div", {"class": "content"})

# save scraped data 
with open('filename.txt', 'w') as file:
    for content in data:
        file.write(str(content))