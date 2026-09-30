We can use the datetime.date class to store dates in ISO 8601 format. We just need to create an instance of datetime.date using the year, month and day. Then, we can convert it to the ISO 8601 format string using isoformat() method of datetime.date. For example:
import datetime
date = datetime.date(2016, 1, 1)
iso_date = date.isoformat()
print(iso_date) // Output: '2016-01-01'