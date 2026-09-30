import random

def random_list(length):
	rand_list = []
	for i in range(length):
		rand_list.append(random.randint(0,100))
	return rand_list