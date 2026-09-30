# Import the necessary libraries
from flask import Flask, request

# Initialize the app
app = Flask(__name__) 
  
@app.route('/post_request_handler', methods = ['POST']) 
def post_request_handler(): 

    # Extract the data from POST request 
    data = request.get_json()  

    # Do something with the data

    # Return a response
    return "Post request handled", 200