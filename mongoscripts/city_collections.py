import json

from pymongo import MongoClient


CLIENT = MongoClient('localhost', 27017)
TRAINING_SET_DB = CLIENT.training_set

SF = [-122.4167, 37.7833]
CHI = [-87.6847, 41.8369]
NY = [-74.0059, 40.7127]
ATX = [-97.75, 30.25]

def partition_collection():
    sf_area = 24510
    chi_area = 24607
    ny_area = 28083
    atx_area = 26521

    geo_america = TRAINING_SET_DB.geo_america
    test = TRAINING_SET_DB.test_set
    sf_collection = TRAINING_SET_DB.sf_tweets
    chi_collection = TRAINING_SET_DB.chi_tweets
    ny_collection = TRAINING_SET_DB.ny_tweets
    atx_collection = TRAINING_SET_DB.atx_tweets    

    locations = {
                    'sf': [SF, sf_area], 
                    'chi': [CHI, chi_area], 
                    'ny': [NY, ny_area], 
                    'atx': [ATX, atx_area]
                }

    query = {
        'coordinates': {
            '$near': {
                '$geometry': {
                    'type': 'Point',
                    'coordinates': None
                },
                '$maxDistance': None
            }
        }
    }

    for location, values in locations.iteritems():
        query['coordinates']['$near']['$geometry']['coordinates'] = values[0]
        query['coordinates']['$near']['$maxDistance'] = values[1]
        for tweet in geo_america.find(query):
            data = {
                '_id': tweet['_id'],
                'id': tweet['id'],
                'coordinates': tweet['coordinates'],
                'user_id': tweet['user']['id']
            }
            if location == 'sf':
                print 'Inserted tweet into SF collection.'
                sf_collection.insert(data)
            if location == 'chi':
                print 'Inserted tweet into CHI collection.'
                chi_collection.insert(data)
            if location == 'ny':
                print 'Inserted tweet into NY collection.'
                ny_collection.insert(data)
            if location == 'atx':
                print 'Inserted tweet into ATX collection.'
                atx_collection.insert(data)



if __name__ == "__main__":
    partition_collection()
