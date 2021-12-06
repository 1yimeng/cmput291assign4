from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client["A4dbNorm"]
artistColl = db["artists"]
#Creating a join between the tracks and artist tables and getting all 
#tracks for each artist by using unwind 
#the match field ensures that we get the values that have release dates greater
# than 1/1/1950.
# once we obtain the entires with release date greater than 1/1/1950 we project the relevant information
#such as objectid, name, track name, track release date 
output = artistColl.aggregate([
    {'$lookup': {'from': 'tracks',
                 'localField': 'tracks',
                 'foreignField': 'track_id',
                 'as': 'tracks'}},
    {'$unwind': '$tracks'},
    {'$match': {
        "tracks.release_date": {"$gt": datetime.datetime(1950, 1, 1)}
    }},
    {"$project": {
        "_id": "$_id",
        "name": "$name",
        "t_name": "$tracks.name",
        "t_release_date": "$tracks.release_date"
    }}
])
#printing the results obtained
for entry in output:
    print(entry)
