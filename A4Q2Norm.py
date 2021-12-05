# db.tracks.aggregate([{$group:{_id: "$artist_ids", avg: {$avg: "$danceability"}}}])
# db.tracks.find({track_id: {$regex: /^70/ }})

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27012')

db = client["A4dbNorm"]

# Create or open the collection in the db
artists_doc = db["artists"]
tracks_doc = db["tracks"]






