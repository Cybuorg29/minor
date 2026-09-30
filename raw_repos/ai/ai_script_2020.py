"""
Find the day of the week corresponding to a given date using calendar module
"""

import calendar

def get_day_of_week(day, month, year):
    dayNumber = calendar.weekday(year,month,day)
    dayName = calendar.day_name[dayNumber] 
    return dayName
    
if __name__ == '__main__':
    day = 25
    month = 12
    year = 2020
    print(get_day_of_week(day, month, year))