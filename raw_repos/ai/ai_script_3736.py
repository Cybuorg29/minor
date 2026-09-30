import statistics

def get_stats(list):
 mean = statistics.mean(list)
 stdev = statistics.stdev(list)
 return mean, stdev

mean, stdev = get_stats(list)
print("Mean:", mean)
print("Standard Deviation:", stdev)