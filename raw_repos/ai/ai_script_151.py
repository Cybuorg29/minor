def compress(string):
    compressed = ""
    count = 1
    for i in range(len(string)):
        if (i+1 < len(string) and string[i] == string[i+1]):
            count += 1
        else:
            if count > 3:
                compressed += string[i] + str(count)
            else:
                compressed += string[i]*count
            count = 1
    return compressed

string = "aaabbcc"
print(compress(string)) # output: a3b2c2