from flask import Flask

app = Flask(__name__)

@app.route("/myroute", methods=["GET"])
def myfunc():
  # write code here

if __name__ == '__main__':
 app.run()