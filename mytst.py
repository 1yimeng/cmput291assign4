from pymongo import MongoClient
import json

# Use client = MongoClient('mongodb://localhost:27012') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = MongoClient('mongodb://localhost:27012')

# Create or open the video_store database on server.
db = client["A4dbNorm"]

with open('artists.json') as f:
    artists = json.load(f)

# print(len(artists))
for artist in artists:
    id = artist["_id"]["$oid"]
    artist["_id"] = 'ObjectId(' + id + ')'

# Create or open the collection in the db
artists_doc = db["artists"]
artists_doc.delete_many({})
artists_doc.insert_many(artists)


with open('tracks.json') as f:
    tracks = json.load(f)

# print(len(tracks))

tracks_doc = db["tracks"]
tracks_doc.delete_many({})
for track in tracks:
    id = track["_id"]["$oid"]
    track["_id"] = 'ObjectId(' + id + ')'

tracks_doc.insert_many(tracks)

