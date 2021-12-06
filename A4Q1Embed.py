from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
art_tracksColl = db['ArtistsTracks']


output = art_tracksColl.aggregate([
    {"$addFields": {
        "num_tracks": {"$size": "$tracks"}
    }},
    {"$project": {
        "artist_id": 1,
        "name": 1,
        "num_tracks": 1
    }}
])

for entry in output:
    if entry["num_tracks"] >= 1:
        print(entry)
