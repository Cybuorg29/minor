from random import choice 

def flip_coin(): 
	result = choice(['Heads', 'Tails']) 

	print(result) 

if __name__ == "__main__": 
	flip_coin()