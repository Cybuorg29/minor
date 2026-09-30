def scrape_frequent_words(url):
    try:
        from bs4 import BeautifulSoup
        from collections import Counter
    
        # Get html from the given url
        html_content = requests.get(url).text
        # Parse the html
        soup = BeautifulSoup(html_content)
        
        # Get all text from the page
        all_texts = soup.find_all(text=True)

        # Extract only words
        words = [word for text in all_texts for word in text.split()]

        # Calculate frequency 
        frequency = dict(Counter(words))
        
        # Return the word with most frequency 
        return max(frequency, key=frequency.get)