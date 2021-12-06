from pymongo import MongoClient
import sys

sys.stdout.reconfigure(encoding = "utf-8")
client = MongoClient('localhost', 27017)

db = client["A4dbNorm"]
artistsColl = db["artists"]
#joining the artist and tracks then we consider all the tracks in the 
#artists, we group by artist id, so that we can group all the songs by one artist
# we then sum the length of all the songs. 
# when printing the output we ensure that the artist field is also included twice in 
# the final output. 
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
