from collections import defaultdict

grouped_dicts = defaultdict(list)

for x in mylist:
 grouped_dicts[x['name']].append(x)