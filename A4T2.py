import json
# import bson
from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
# load and add the artist file
artistColl = db['Artists']
artistColl.delete_many({})

with open('artists.json', encoding='utf-8') as file:
    file_data = json.load(file)

l = []
for id in file_data:
    id["_id"] = id["_id"]["$oid"]
    l.append(id)

if isinstance(l, list):
    artistColl.insert_many(l)
else:
    artistColl.insert_one(l)

# load and add the track file
trackColl = db['Tracks']
trackColl.delete_many({})
with open('tracks.json', encoding='utf-8') as file:
    file_data = json.load(file)

l = []
for id in file_data:
    id["_id"] = id["_id"]["$oid"]
    l.append(id)

if isinstance(file_data, list):
    trackColl.insert_many(l)
else:
    trackColl.insert_one(l)

art_tracksColl = db['ArtistsTracks']
db.Artists.aggregate([
    {'$lookup': {'from': 'track',
                 'localField': 'artist_id',
                 'foreignField': 'artist_ids',
                 'as': 'results'}},
    {'$out': "ArtistsTracks"}
])  # .pretty()

# drop other collections
artistColl.drop()
trackColl.drop()
