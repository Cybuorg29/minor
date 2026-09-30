def parseDate(date_string):
    date_list = date_string.split()
    month_dict = {
        'Jan': '01', 
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    day = date_list[0]
    month = month_dict[date_list[1]]
    year = date_list[2]

    return day + "-" + month + "-" + year