from flask import Flask, request

app = Flask(__name__)

users = {"John": "123456", "Jenny": "456789"}

@app.route('/', methods=['GET'])
def root():
    if request.authorization and request.authorization.username in users \
            and request.authorization.password == users[request.authorization.username]:
        return 'Authentication successful!' 
    else:
        return 'Authentication failed!'
        
if __name__ == '__main__':
    app.run(debug=True)