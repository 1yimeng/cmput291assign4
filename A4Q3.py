import pymongo
import datetime
from bson.json_util import loads
from pymongo import collection
import mongodb_example
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27012')
db = client["A4dbNorm"]
artists_doc = db["artists"]
tracks_doc = db["tracks"]

tracks_doc.aggregate([{"$unwind": "$tracks"}])
tracks_cursor = tracks_doc.aggregate([
    {"$group": {
        "_id": "artist_id",
        "total_length": {"$sum": "$duration"}}},
    {"artist_id": {"artist_id"}}

])
for entry in tracks_cursor:
    print(entry)
