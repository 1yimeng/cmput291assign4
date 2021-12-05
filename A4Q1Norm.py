# db.artists.find({ num_tracks: { $gte: 1}}, {followers: 0, genres: 0, popularity: 0})
# db.artists.aggregate([{$addFields: {"num_tracks": { $size: "$tracks"}}}])
#  db.artists.aggregate([{$addFields: {"num_tracks": { $size: "$tracks"}}}, {$project : { followers: 0, genres: 0, popularity: 0, tracks: 0}}])
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27012')

db = client["A4dbNorm"]

# Create or open the collection in the db
artists_doc = db["artists"]
tracks_doc = db["tracks"]

add_numtracks = { "$addFields": {"num_tracks": { "$size": "$mytracks"}}}

projection = {"$project" : { "artist_id": 1, "name": 1, "num_tracks": 1}}

result = artists_doc.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'mytracks'}},
    add_numtracks,
    projection,
])

for x in result:
    if x["num_tracks"] >= 1:
        print(x)





