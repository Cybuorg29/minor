def parse_ingredients(html): 
    soup = BeautifulSoup(html, 'html.parser') 
    ingredients = [li.text for li in soup.find_all('li')] 
    return ingredients