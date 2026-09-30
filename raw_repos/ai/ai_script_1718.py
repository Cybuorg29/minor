import re

regex = re.compile(r"^[a-z]+$")

string1 = "string1"
string2 = "string2"

if regex.match(string1) and regex.match(string2):
    if string1 == string2:
        print("The strings are equal")
    else:
        print("The strings are not equal")