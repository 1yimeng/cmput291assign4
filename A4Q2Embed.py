from pymongo import MongoClient
import sys

sys.stdout.reconfigure(encoding = "utf-8")
client = MongoClient('localhost', 27017)

db = client["A4dbEmbed"]
art_tracksColl = db['ArtistsTracks']

output = art_tracksColl.aggregate([
    {'$unwind': '$tracks'},
    {'$match': {'tracks.track_id': {'$regex': "^70.*"}}},
    {'$group': {
        '_id': '', 'avg_danceability': {'$avg': '$tracks.danceability'}
    }}
])

for entry in output:
    print(entry)
