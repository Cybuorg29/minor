"""
Calculate the number of days since January 1st, 1971 until the given date
"""

import datetime as dt

def num_days(date_str):
    datetime_object = dt.datetime.strptime(date_str, "%B %d, %Y").date()
    ref_date = dt.datetime(1971, 1, 1).date()
    return (datetime_object - ref_date).days

if __name__ == '__main__':
    print(num_days('May 3rd, 2012'))