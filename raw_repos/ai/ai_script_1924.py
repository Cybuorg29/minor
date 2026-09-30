from bs4 import BeautifulSoup 
  
# data stored in a string 
html_doc = """ 
<html><head><title>Parser Demo</title></head> 
<body> 
<h1>This is Heading1</h1> 
<h2>This is Heading2</h2> 
</body></html> 
"""
  
# passing the html document to 
# BeautifulSoup() for parsing 
soup = BeautifulSoup(html_doc, 'html.parser') 
  
# parsing tags from the document 
tags = [tag.name for tag in soup.find_all()] 

print(tags)