import re 

pattern = re.compile(r'(?P<name>[\w ]+); (?P<dob>[\d/]+); (?P<addr>[\w ]+[,][\w ]+)')
match = pattern.search('John Smith; 10/03/1994; 9 Hall Street, Anytown') 
name = match.group('name') 
dob = match.group('dob') 
addr = match.group('addr')