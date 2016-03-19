import json

import sys

from application import get_live_tweets_thread
from dateutil.parser import parse
from django.http import HttpResponse
from lima.settings import TRAINING_SET_DB
from threading import Thread, ThreadError

"""
 TODO: Instead of models, we use pymongo and the config can be handled
 somewhere else
"""


# Create your views here.
def maps(request):
    """
    Args:
        request: Handles a POST request where the request contains a
                 JSON object. JSON object with 'stream' = False will instantiate
                 websocket. Performs query from AJAX request otherwise.
                 JSON Object:
                 {
                    'stream': boolean,
                    'keywords': list[str],
                    'start_date': str,
                    'end_date': str
                 }
                TODO: finish docs
    Returns: { 'coordinates', 'LIMA score', 'color' }
    """
    if request.method == 'POST':
        get_stream = request.POST.get('stream')
        keywords = request.POST.get('keywords')
        print keywords
        if get_stream:
            print "Starting real-time stream"
            try:
                thread = Thread(target=get_live_tweets_thread, args=(keywords,))
                thread.daemon = True
                thread.start()
            except ThreadError:
                print 'Something went horribly wrong with this thread mate'
            response = {'sup': 'brah'}
            print response['sup']
            return HttpResponse(json.dumps(response),
                                content_type='application/json')
            # start_date = parse(request.POST.get('start_date'))
            # end_date = parse(request.POST.get('end_date'))

            # TODO: Gather location & LIMA score from DB within this range
            # date_filter = {'created_at', {'$gte': start_date, '$lt': end_date}}

            # geo_america = TRAINING_SET_DB.geo_america
            # resp_data = geo_america.find_one()

    return HttpResponse({json.dumps({'worked': 'yes'})},
                        content_type='application/json')


def stats(request):
    """
    Args:
        request:

    Returns:
    """
    return HttpResponse(json.dumps({}), content_type='application/json')


def tweets(request):
    """
    Args:
        request:

    Returns:
    """
    return
