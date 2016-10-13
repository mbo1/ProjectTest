import pymongo
from pymongo import MongoClient

# Connection to Mongo DB
client = ''
db = ''
try:
    client = MongoClient('mongodb://192.168.75.5:27017/')
    db = client.test
    print (client.database_names())
    print ("Connected successfully!!!")
except pymongo.errors.ConnectionFailure as e:
   print ("Could not connect to MongoDB: %s" % e) 


cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

for document in cursor:
    print(document)