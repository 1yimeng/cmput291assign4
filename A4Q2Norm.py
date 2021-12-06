from pymongo import MongoClient
import sys

sys.stdout.reconfigure(encoding = "utf-8")
client = MongoClient('localhost', 27017)

db = client["A4dbNorm"]
artistsColl = db["artists"]

result = artistsColl.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}},
    {'$unwind': '$tracks'},
    {'$match': {'tracks.track_id': {'$regex': "^70.*"}}},
    {'$group': {
        '_id': '', 'avg_danceability': {'$avg': '$tracks.danceability'}}
     }
])

for i in result:
    print(i)
