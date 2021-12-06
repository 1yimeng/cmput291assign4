from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["A4dbEmbed"]
art_tracksColl = db["ArtistsTracks"]

output = art_tracksColl.aggregate([
    {"$unwind": "$tracks"},
    {"$group": {
        "_id": "$artist_id",
        "total_length": {"$sum": "$tracks.duration"}
    }},
    {"$addFields": {"artist_id": "$_id"}}
])

for entry in output:
    print(entry)
