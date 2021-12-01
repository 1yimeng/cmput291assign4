import json
# import bson
from pymongo import MongoClient
client = MongoClient()

db = client["A4dbEmbed"]
# load and add the artist file
collection = db['ArtistsTracks']
collection.delete_many({})
with open('artists.json') as file:
    file_data = json.load(file)
# print(file_data[0])
# print(type(file_data))
l = []
for id in file_data:
    id["_id"] = id["_id"]["$oid"]
    l.append(id)
    
if isinstance(l, list):
    collection.insert_many(l)  
else:
    collection.insert_one(l)

# load and add the track file
Collect = db['track']
Collect.delete_many({})
with open('tracks.json') as file:
    file_data = json.load(file)

l = []
for id in file_data:
    id["_id"] = id["_id"]["$oid"]
    l.append(id)

if isinstance(file_data, list):
    Collect.insert_many(l)  
else:
    Collect.insert_one(l)



# db.artists.aggregate(
#     [
#         {
#             $lookup:{
#                 localField:"tracks",
#                 from:"tracks",
#                 foreignField:"track_id",
#                 as:""
#             }
#         }
#     ]
# )


# ArtistsTracks = artists.aggregate(
#     [    {
#             “$lookup”:{
#                 "from":"tracks",
                
#                 "foreignField":"artist_ids",
#                 "as":"artist_tracks"
#             }
#         }
#     ]
# )
# collection.delete_many({})
result = db.ArtistsTracks.aggregate([{
       '$lookup' : {'from': 'track',
       'localField': 'artist_id',
       'foreignField': 'artist_ids',
       'as': 'results' }
}])#.pretty()

# for r in result:
#     print(r)
# collection.delete_many({})
collection.insert_many(result)