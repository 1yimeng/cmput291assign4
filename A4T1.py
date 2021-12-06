from pymongo import MongoClient
from bson.json_util import loads

# Use client = MongoClient('mongodb://localhost:27012') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = MongoClient('localhost', 27017)
db = client["A4dbNorm"]

with open('artists.json', encoding='utf-8') as f:
    artists = loads(f.read())

# Create or open the collection in the db
artists_doc = db["artists"]
artists_doc.delete_many({})
artists_doc.insert_many(artists)


with open('tracks.json', encoding='utf-8') as f:
    tracks = loads(f.read())

tracks_doc = db["tracks"]
tracks_doc.delete_many({})

tracks_doc.insert_many(tracks)
