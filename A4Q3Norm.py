from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["A4dbNorm"]
artistsColl = db["artists"]

output = artistsColl.aggregate([
    {'$lookup': {
        'from': 'tracks',
        'localField': 'tracks',
        'foreignField': 'track_id',
        'as': 'tracks'
    }},
    {"$unwind": "$tracks"},
    {"$group": {
        "_id": "$artist_id",
        "total_length": {"$sum": "$tracks.duration"}
    }},
    {"$addFields": {"artist_id": "$_id"}}
])

for entry in output:
    print(entry)
