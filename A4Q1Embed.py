from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
artiststracks = db['ArtistsTracks']

add_numtracks = { "$addFields": {"num_tracks": { "$size": "$tracks"}}}

projection = {"$project" : { "artist_id": 1, "name": 1, "num_tracks": 1}}

numtrack_return = artiststracks.aggregate([add_numtracks, projection])

for x in numtrack_return:
    if x["num_tracks"] >= 1:
        print(x)
