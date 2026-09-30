def get_user_name(user_id):
    sql_query = "SELECT first_name, last_name FROM user_profiles WHERE user_id = ?"
    user = cursor.execute(sql_query, (user_id,))
    return user[0] + " " + user[1]