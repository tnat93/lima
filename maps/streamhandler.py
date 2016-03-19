import os
import sys

from json import dumps, load, loads
from tweepy import API, StreamListener, streaming, OAuthHandler

CONSUMER_KEY = 'QtAh3vSjkQdniyobrxF6armTa'
CONSUMER_SECRET = 'latUsH07Pz5W7jyp40URwlkNTBnzByX9H8VctaHbP4siDqhjsU'
ACCESS_TOKEN = '434673129-KAErcwnbmgG2usXPtpxihipjOl0HyTK8Z9T20tFO'
ACCESS_TOKEN_SECRET = 'oATFryF61579GFKyx2TojscOrUCz4SoDOiAZLkhkrA76f'

AUTH = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class ApplicationStream(StreamListener):
    def __init__(self, api):
        super(StreamListener, self).__init__()
        self.api = api

    def on_data(self, raw_data):
        # TODO: Perform location inference and sentiment analysis scoring, then write to file.
        data = loads(raw_data)
        text = data['text'].encode('ascii', 'ignore').lower()
        tweet_data = {'id': data['id'], 'text': text}
        print text
        data_list = []
        if not os.path.isfile('tweet_data.json'):
            data_list.append(tweet_data)
            with open('tweet_data.json', 'w') as outfile:
                outfile.write(dumps(data_list, indent=3))
        else:
            with open('tweet_data.json') as feed:
                feeds = load(feed)
            feeds.append(tweet_data)
            with open('tweet_data.json', 'w') as outfile:
                outfile.write(dumps(feeds, indent=3))


if __name__ == '__main__':
    keywords = None
    try:
        keywords = sys.argv[1:]
    except TypeError:
        print >> sys.stderr, "Caught TypeError"
    api = API(AUTH)
    stream = streaming.Stream(AUTH, ApplicationStream(api))

    while True:
        print 'Starting new stream'
        if keywords is not None:
            stream.filter(languages=['en'], track=keywords)