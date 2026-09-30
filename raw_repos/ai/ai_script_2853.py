import bs4 

html = "<html><h1>Heading 1</h1><h2>Heading 2</h2><h2>Heading 3</h2></html>" 

soup = bs4.BeautifulSoup(html, 'html.parser') 

h2_list = soup.find_all('h2')
print(h2_list)