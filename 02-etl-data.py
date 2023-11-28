import pymongo
import pandas as pd

client = pymongo.MongoClient(
    "mongodb://username:password@localhost:27017/?authSource=admin"
)
db = client["ecommerce"]
