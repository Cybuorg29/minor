def check_restaurant_availability(restaurant_status):
    day = datetime.date.today().strftime("%A").lower()
    return restaurant_status[day] == "open"