from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
artiststracks = db['ArtistsTracks']

#     {'$group': {'_id': 
#     {'new_track_id':{'$track':{'$track_id':{'$regex': "^70"}}}},
#                  'average':{'$avg':"$danceability"}}
#     }])

    # artiststracks.aggregate([
    # {'$group': {'_id': 
    # {'new_track_id':{'$tracks':{'$track_id':{'$regex': "^70"}}}},
    #              'average':{'$avg':"$danceability"}}
    # }])

cursor = artiststracks.aggregate([
    {'$unwind':'$tracks'},
    {'$match':{'tracks.track_id':{'$regex': "^70.*"}}},
    {'$group':{
        '_id':'','avg_danceability':{'$avg':'$tracks.danceability'}}
    }
    ])

    
# print(new_output)    
# print(list(cursor))  
for document in cursor:
    print(document)
#     {$group:
# {_id:
# {new_track_id:{"$regex: /^70/"}}, 
# average:{$avg:"$danceability"}
# }}])