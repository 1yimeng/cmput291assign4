import pymongo
import datetime
from bson.json_util import loads
from pymongo import collection
import mongodb_example
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Create or open the video_store database on server.
db = client["A4dbNorm"]
Artists = db["artists"]
Tracks = db["tracks"]
newCollection = Artists.aggregate([
    {'$unwind': '$tracks'},
    {'$lookup': {'from': 'Tracks'},
     '$match': {"$eq": ["$tracks", "$track_id"],
                "$gt": ["$release_date", datetime.datetime(1950, 1, 1)]}},
    {"$project": {"_id": "$_id", "name": "$name", "t_name": "$tracks.name",
                  "t_release_date": "$tracks.release_date"}}

])


for entry in newCollection:
    # newCollection.insertOne(tracksCursor.next())

    print(entry)


# tracks_doc.aggregate([{
#     '$lookup':
#     {
#         'from': "artists",
#         'localfield': "artist_id",
#         'foreignField': "tracks",
#         'as': "artist_name"
#     }

# }])
