import pymongo
import datetime
from bson.json_util import loads
from pymongo import collection
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["A4dbNorm"]
artists_doc = db["artists"]
tracks_doc = db["tracks"]
# why did we need to do find

artists_doc.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}
     },
    {"$out": "newcoll"}
])
newcollection = db["newcoll"]
output = newcollection.aggregate([
    {"$unwind": "$tracks"},
    {
        "$group": {
            "_id": "$artist_id",
            "total_length": {"$sum": "$tracks.duration"}
            # "artist_id": {"$min": "$artist_ids"}
        }


    },
    {"$addFields": {"artist_id": "$_id"}}
])

for entry in output:
    print(entry)
newcollection.drop()
