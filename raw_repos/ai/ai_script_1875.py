from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
h1_text = soup.find("h1").text
print(h1_text)
# Output: Hello World!