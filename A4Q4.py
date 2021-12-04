import pymongo
import datetime
from bson.json_util import loads
from pymongo import collection
import mongodb_example
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Create or open the video_store database on server.
db = client["A4dbNorm"]
artists_doc = db["artists"]
tracks_doc = db["tracks"]
# Note: in the query 4 exapmple .datetime is used to save it

tracksCursor = tracks_doc.find(
    {"release_date": {"$gt": datetime.datetime(1950, 1, 1)}}).pretty()
# newCollection = db["Tracks1"]
for entry in tracksCursor:
    # newCollection.insertOne(tracksCursor.next())

    artists_doc.find({"artist_id": entry["artist_id"]})
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
