import datetime

def get_difference_in_seconds(timestamp1, timestamp2):
    datetime1 = datetime.datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    difference = (datetime2 - datetime1).total_seconds()
    return difference