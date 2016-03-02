import json

import sys

from application import connect_to_application
from dateutil.parser import parse
from django.http import HttpResponse
from lima.settings import TRAINING_SET_DB, APPLICATION_SERVER_HOST, \
    APPLICATION_SERVER_PORT
from threading import Thread

"""
 TODO: Instead of models, we use pymongo and the config can be handled
 somewhere else
"""


# TODO: Integrate Spark tasks.


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
        print "I'm here dude"
        print request
        get_stream = request.POST.get('stream')
        keywords = request.POST.get('keywords')
        print get_stream + ' ' + keywords
        if get_stream:
            # TODO: Error check to see if stream is already started with same user
            print "Starting real-time stream"
            success = False
            conn_args = (
                APPLICATION_SERVER_HOST, APPLICATION_SERVER_PORT, keywords,
                success)
            # Send signal to stream handler to instantiate websocket connection
            # and begin streaming data.
            try:
                thread = Thread(target=connect_to_application, args=conn_args)
                thread.start()
            except:
                print >> sys.stderr, "Could not start thread"
            response = {}
            if success:
                response['status'] = 'Successfully started stream'
            else:
                response['status'] = 'Something went wrong dude'
            return HttpResponse(json.dumps(response),
                                content_type='application/json')
        start_date = parse(request.POST.get('start_date'))
        end_date = parse(request.POST.get('end_date'))

        # TODO: Gather location & LIMA score from DB within this range
        date_filter = {'created_at', {'$gte': start_date, '$lt': end_date}}

        geo_america = TRAINING_SET_DB.geo_america
        resp_data = geo_america.find_one()

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
