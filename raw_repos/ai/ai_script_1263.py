def compressString(s): 
	comp_string = ""
	count = 1
	for i in range(len(s) - 1): 
		if(s[i] == s[i+1]): 
			count+= 1
		else: 
			comp_string += s[i] + str(count) 
			count = 1
	comp_string += s[i] + str(count) 
	return comp_string