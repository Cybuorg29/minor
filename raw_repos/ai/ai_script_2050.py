"""
Construct a dialogue bot using natural language processing techniques
"""
import nltk

# Define a simple set of rules to respond to the user's input
def respond(input):
	if input == "hello" or input == "hi":
		return("Hello. How can I help you today?")
	elif input == "goodbye":
		return("Goodbye! Have a nice day.")
	else:
		return("I'm sorry, I don't understand what you said.")

# Tokenize the input string and call the respond function
def chatbot(input_string):
	tokens = nltk.word_tokenize(input_string)
	response = respond(' '.join(tokens))
	return response

if __name__ == '__main__':
	print(chatbot("Hello!"))