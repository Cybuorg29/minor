@app.route('/items', methods = ['GET'])
def display_items():
 # write your code here
 items = []
 # query the database
 items = db.session.query(Items).all()
 # return the list of items
 return jsonify(items)