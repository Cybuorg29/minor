from collections import Counter

def most_common_phrase(string_list):
    c = Counter(string_list)
    return c.most_common(1)[0][0]

most_common_phrase(["hello world", "hello", "hello world again"])
# output: 'hello world'