from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]

art_tracksColl = db["ArtistsTracks"]

# not sure how to get the last column of artist_id??
result = art_tracksColl.aggregate(
    [
        {"$unwind": "$tracks"},

        {"$group": {
            "_id": "$artist_id",
            "total_length": {"$sum": "$tracks.duration"}
        }},

        {"$addFields": {"artist_id": "$_id"}}
    ]
)

for r in result:
    print(r)
