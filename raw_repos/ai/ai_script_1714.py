def replace_vowels(string):
	vowels = "aeiou"
	result = ""
	for char in string:
		if char in vowels:
			char = "*"
		result += char
	return result