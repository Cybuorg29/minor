def daysBetween(date1, date2): 
    startDate = pd.to_datetime(date1) 
    endDate = pd.to_datetime(date2)
    delta = endDate - startDate
    return delta.days