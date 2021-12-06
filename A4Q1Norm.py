from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["A4dbNorm"]
artistsColl = db["artists"]

output = artistsColl.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'mytracks'}},
    {"$addFields": {
        "num_tracks": {"$size": "$mytracks"}
    }},
    {"$project": {
        "artist_id": 1,
        "name": 1,
        "num_tracks": 1
    }}
])

for entry in output:
    if entry["num_tracks"] >= 1:
        print(entry)
