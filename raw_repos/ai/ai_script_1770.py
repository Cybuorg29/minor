@app.route('/store_data', methods=['POST'])
def store_data():
 data = request.get_json()
 
 first_name = data['first_name']
 last_name = data['last_name']
 
 db.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
 db.commit()
 
 return jsonify(message="Data stored successfully.")