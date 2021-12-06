from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient('localhost', 27017)
db = client["A4dbEmbed"]

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


result = artists_doc.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}},
])

art_tracksColl = db['ArtistsTracks']
art_tracksColl.delete_many({})
art_tracksColl.insert_many(result)

# drop other collections
artists_doc.drop()
tracks_doc.drop()
