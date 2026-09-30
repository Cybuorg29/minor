import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

collection.insert_one({
    "name": "John Doe",
    "age": 25,
    "city": "New York"
})