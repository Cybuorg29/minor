"""
Write a Python script to parse given web pages and extract links from it
"""

from bs4 import BeautifulSoup
import requests

def extract_links(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

if __name__ == '__main__':
    print(extract_links('https://example.com'))