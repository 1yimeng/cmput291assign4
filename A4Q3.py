import pymongo
import datetime
from bson.json_util import loads
from pymongo import collection
import mongodb_example
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client["A4dbNorm"]
artists_doc = db["Artists"]
tracks_doc = db["Tracks"]
# why did we need to do find
Artist = artists_doc.find({})
Tracks = tracks_doc.find({})

artists_doc.aggregate({
    {'$lookup': {'from': 'Tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}
     },
    {"$out": "newcoll"}
})
newcollection = db["newcoll"]
output = newcollection.aggregate({
    {"$unwind": "$tracks"},
    {
        "$group": {
            "_id": "$artist_ids",
            "total_length": {"$sum": "$duration"},
            "artist_id": {"$min": "$artist_ids"}
        }
    }
})

for entry in output:
    print(entry)
newcollection.drop()
