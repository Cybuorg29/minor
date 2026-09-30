import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# loading data
data = [('This is an email about about a promotion', 'spam'),
	('We want to transfer money to your account', 'spam'),
	('This email is about programming', 'not_spam'),
	('There is a new version of python', 'not_spam'),
]

# extracting features
X, y = [], []
for feat, lab in data:
	X.append(feat)
	y.append(lab)

cv = CountVectorizer()
X_vect = cv.fit_transform(X)

# training the model
model = MultinomialNB()
model.fit(X_vect, y)

# predicting
prediction = model.predict(cv.transform(["This is an email about a discount sale"]))
print(prediction)

# Output
['spam']