from collections import Counter

def get_most_frequent_value(mylist):
    counted_list = Counter(mylist)
    return counted_list.most_common(1)[0][0]

most_frequent_value = get_most_frequent_value(mylist)
print(most_frequent_value)

# Output
# 4