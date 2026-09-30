def freq_dict(string):
 freq = {}
 for c in string:
 if c in freq:
 freq[c] += 1
 else:
 freq[c] = 1
 return freq