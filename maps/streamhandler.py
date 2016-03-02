from json import loads
from lima.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
    ACCESS_TOKEN_SECRET
from tweepy import StreamListener, streaming


class ApplicationStream(StreamListener):
    def __init__(self, api):
        super(StreamListener, self).__init__()
        self.api = api

    def on_data(self, raw_data):
        # TODO: Perform location inference and sentiment analysis scoring, then write to file.
        data = loads(raw_data)
        return


