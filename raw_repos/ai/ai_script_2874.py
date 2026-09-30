from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>This is a heading 1</h1>
    <h2>This is a heading 2</h2>
    <h1>This is another heading 1</h1>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

h1_tags = soup.find_all('h1')
for tag in h1_tags:
    print(tag)