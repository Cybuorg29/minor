import datetime
def hello_world():
    print("Hello world!")
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))