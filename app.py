import oauth2 as oauth, sys

from urllib import urlencode

settings = {
    'consumer_key': 'nT6Rj3LJrtKDdsBepWbGaoydR',
    'consumer_secret': 'pPMvJRExPtDr0Hp7C7OMjjf1sM1zBVoAIHg0yecXVSIsBOzk5i',
    'token': '1864732598-QO0wi40n5JPPBVXiptoMCrrsTlgwqWHMe1SMIcZ',
    'token_secret': 'L2SFsTYHuhDtvQDZjzrbT8WhvpcWFHGRKi1ch8GwjQs',
}

class Twitter:
    def __init__(self, **kargs):
        self.api_endpoint = 'https://api.twitter.com/1.1/'
        consumer = oauth.Consumer(key=kargs['consumer_key'], secret=kargs['consumer_secret'])
        token = oauth.Token(key=kargs['token'], secret=kargs['token_secret'])
        self.client = oauth.Client(consumer, token)

    def tweet(self, status):
        return self.client.request(self.api_endpoint + 'statuses/update.json?' + urlencode({'status': status}), method='POST')

twitter = Twitter(**settings)
print twitter.tweet(sys.argv[1])
