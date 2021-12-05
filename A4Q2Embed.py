from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
artiststracks = db['ArtistsTracks']

cursor = artiststracks.aggregate([
    {'$unwind':'$tracks'},
    {'$match':{'tracks.track_id':{'$regex': "^70.*"}}},
    {'$group':{
        '_id':'','avg_danceability':{'$avg':'$tracks.danceability'}}
    }
    ])

 
for document in cursor:
    print(document)
