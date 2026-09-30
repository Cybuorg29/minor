import nltk
from nltk.corpus import stopwords

txt = "I am wondering what is the best way to learn English."
words = nltk.word_tokenize(txt)
filtered_words = [w for w in words if not w in stopwords.words('english')] 
  
print(filtered_words)