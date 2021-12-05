from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]

art_tracksColl = db["ArtistsTracks"]

result = art_tracksColl.aggregate(
    [
        {"$unwind": "$tracks"},

        {"$match": {  # datetime.datetime(1950, 1, 1)
            "$tracks.release_date": {"$gt": datetime.datetime(1950, 1, 1)}}
         },

        {"$project": {
            "_id": "$tracks._id",
            "name": "$name",
            "t_name": "$tracks.name",
            "t_release_date": "$tracks.release_date"
        }}


    ]
)
# {"$gt": datetime.datetime(1950, 1, 1)}}).pretty()

for r in result:
    print(r)
