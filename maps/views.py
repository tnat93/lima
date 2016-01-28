from django.shortcuts import render

"""
 TODO: Instead of models, we use pymongo and the config can be handled
 somewhere else
"""


# Create your views here.
def maps(request):
    """
    Args:
        request: Handles a POST request where the request contains a
                 JSON object. JSON object with 'ajax' = False will instantiate
                 websocket. Performs query from AJAX request otherwise.
                # TODO finish docs
    Returns: { 'coordinates', 'LIMA score', 'color' }
    """
    return


def stats(request):
    """
    Args:
        request:

    Returns:
    """
    return


def tweets(request):
    """
    Args:
        request:

    Returns:
    """
    return
