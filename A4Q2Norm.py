from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27012')

db = client["A4dbNorm"]

# Create or open the collection in the db
artists_doc = db["artists"]
tracks_doc = db["tracks"]

result = artists_doc.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}},
    {'$unwind':'$tracks'},
    {'$match':{'tracks.track_id':{'$regex': "^70.*"}}},
    {'$group':{
        '_id':'','avg_danceability':{'$avg':'$tracks.danceability'}}
    }
])

for i in result:
    print(i)





