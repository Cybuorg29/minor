def get_day(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date.weekday()
    return days[day_index]

print(get_day(date(2020, 10, 13)))