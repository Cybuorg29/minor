def filter_keywords(text, keywords):
  words = text.split()
  filtered_words = [word for word in words if word not in keywords]
  return ' '.join(filtered_words)
  
text = 'This is a text containing some keywords'
keywords = ['keywords', 'text']

print(filter_keywords(text, keywords))