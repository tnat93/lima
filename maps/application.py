"""
    Thread functions called by API endpoints from views.py
    Author: Bryan Deloeste
"""
import json

from bson import json_util
from lima.settings import TRAINING_SET_DB, PUSHER
from pymongo import DESCENDING
from threading import Thread, ThreadError
from time import sleep, time

DEBUG_COLL = 'geo_america'

ONE_SECOND_MS = 1000
ONE_MINUTE_MS = 60000
TEN_MIN_MS = 600000
ONE_HOUR_MS = 3600000


def get_current_time_ms():
    """

    Returns: Current Epoch time in milliseconds.

    """
    return int(round(time() * 1000))


def clean_buffer_thread(buff, coll):
    """
    This thread clears the dictionary referenced by `buff`
    and removes old tweet documents from the `coll`
    collection every ten minutes.

    Args:
        buff: Dictionary of `stream_buffer` documents where
              keys are document `_id`s and values correspond
              to whether the document has been sent to the
              client.
        coll: MongoDB Collection object.
    """
    while True:
        print 'Deleting old stuff...'
        buff.clear()
        delete_query = {'time_inserted': {'$lt': get_current_time_ms() - TEN_MIN_MS}}
        result = coll.remove(delete_query)
        print 'Deleted: ', result
        sleep(600)


def get_live_tweets_thread(keywords):
    """
    Sends geo-location and sentiment analysis information to the client
    via `tweet_stream` Pusher socket channel.

    `stream_buffer` holds previous ten minutes worth of data.

    Args:
        keywords: Takes in list of keywords that are used to query
        database.
    Returns: None
    """
    pusher = PUSHER
    stream_collection = TRAINING_SET_DB['stream_buffer']

    if stream_collection.count() == 0:
        print 'There\'s nothing in the stream for you'
        return

    seen = {}
    try:
        thread = Thread(target=clean_buffer_thread, args=(seen, stream_collection, ))
        thread.daemon = True
        thread.start()
    except ThreadError, v:
        print 'Sorry, some thread error happened', v

    while True:
        print 'Gathering data with keywords: ', keywords
        sleep(1)
        tweet_buffer = stream_collection.find(
            {'$text': {'$search': keywords}}).sort('time_inserted', DESCENDING)
        for tweet in tweet_buffer:
            current_time_ms = get_current_time_ms()
            previous_ten_min_ms = current_time_ms - TEN_MIN_MS
            tweet_inserted_time_ms = tweet['time_inserted']
            tweet_id = tweet['_id']
            if tweet_inserted_time_ms < previous_ten_min_ms:
                break
            if seen.get(tweet_id) is None:
                seen[tweet_id] = 1
                data = {'timestamp': current_time_ms, 'data': tweet}
                # print 'Sent tweets at', str(current_time_ms)
                pusher.trigger(channels='lima', event_name='tweet_stream',
                               data=json.dumps(data, default=json_util.default))


if __name__ == '__main__':
    get_live_tweets_thread('hello')
