def is_substring_present(string, sub_string):
 for i in range(len(string)):
 if string[i : (i + len(sub_string))] == sub_string:
 return True
 return False