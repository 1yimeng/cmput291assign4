from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27012')

db = client["A4dbNorm"]

# Create or open the collection in the db
artists_doc = db["artists"]
tracks_doc = db["tracks"]

add_numtracks = { "$addFields": {"num_tracks": { "$size": "$tracks"}}}

projection = {"$project" : { "artist_id": 1, "name": 1, "num_tracks": 1}}

numtrack_return = artists_doc.aggregate([add_numtracks, projection])

for x in numtrack_return:
    if x["num_tracks"] >= 1:
        print(x)