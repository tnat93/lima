"""
    Thread functions called by API endpoints from views.py
    Author: Bryan Deloeste
"""
import json

from bson import json_util
from lima.settings import TRAINING_SET_DB, PUSHER
from pymongo import DESCENDING
from time import sleep, time

DEBUG_COLL = 'geo_america'


def get_live_tweets_thread(keywords):
    """
    Args:
        keywords: Takes in list of keywords that are used to query
        database.
    Returns: None
    """
    pusher = PUSHER
    stream_collection = TRAINING_SET_DB[DEBUG_COLL]

    if stream_collection.count() == 0:
        print 'There\'s nothing in the stream for you'
        return

    while True:
        print 'Gathering data with keywords: ', keywords
        sleep(1)
        tweet_buffer = stream_collection.find(
            {'$text': {'$search': keywords}}).sort(
            'timestamp_ms', DESCENDING)
        current_time_ms = int(round(time() * 1000))
        stream_buffer = []
        for tweet in tweet_buffer:
            time_ms = int(tweet['timestamp_ms'])
            if time_ms > current_time_ms:
                stream_buffer.append(tweet)
            else:
                break
        data = {'timestamp': current_time_ms, 'data': stream_buffer}
        print 'Sent: ', len(data['data']), 'tweets at', data['timestamp']
        pusher.trigger(channels='lima', event_name='tweet_stream',
                       data=json.dumps(data, default=json_util.default))


if __name__ == '__main__':
    get_live_tweets_thread('hello')
