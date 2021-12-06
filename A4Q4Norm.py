from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client["A4dbNorm"]
artistColl = db["artists"]

output = artistColl.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}},
    {'$unwind': '$tracks'},
    {'$match': {
        "tracks.release_date": {"$gt": datetime.datetime(1950, 1, 1)}
    }},
    {"$project": {
        "_id": "$_id",
        "name": "$name",
        "t_name": "$tracks.name",
        "t_release_date": "$tracks.release_date"
    }}
])

for entry in output:
    print(entry)
