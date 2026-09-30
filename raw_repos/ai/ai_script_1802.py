def generate_strings(set, k): 
	strings = [] 
	n = len(set) 
	
	def generate_strings_recur(sub, count): 
		
		# Base cases 
		if count == 0 : 
			strings.append(sub) 
			return
		
		for i in range(n): 
			
			# Next character of string to be 
			# formed 
			new_sub = sub + set[i] 
			
			# Recursion call 
			generate_strings_recur(new_sub, 
								count-1) 
	
	count = k 
	sub = "" 
	
	# Call to generate all strings of length k 
	generate_strings_recur(sub, count) 
	
	return strings