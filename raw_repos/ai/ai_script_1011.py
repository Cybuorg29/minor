import datetime

def convert_to_timestamp(date_string):
    """Write a code to convert a given date string into a timestamp."""
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    timestamp = datetime.datetime.timestamp(date_object)
    return timestamp

convert_to_timestamp("2020-07-24 14:50:00") # Outputs 1595538200.0