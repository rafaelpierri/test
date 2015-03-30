import oauth2 as oauth

CONSUMER_KEY = 'nT6Rj3LJrtKDdsBepWbGaoydR'
CONSUMER_SECRET = 'pPMvJRExPtDr0Hp7C7OMjjf1sM1zBVoAIHg0yecXVSIsBOzk5i2'
ACCESS_TOKEN = '1864732598-QO0wi40n5JPPBVXiptoMCrrsTlgwqWHMe1SMIcZ'
ACCESS_TOKEN_SECRET = 'L2SFsTYHuhDtvQDZjzrbT8WhvpcWFHGRKi1ch8GwjQs'
URL = 'https://api.twitter.com/1.1/'


def oauth_req(url, key, secret, http_method="GET", body=''):
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=body)
    return resp, content


def tweet(value):
    resp, content = oauth_req(URL + 'statuses/update.json?status=' + value,
                              ACCESS_TOKEN,
                              ACCESS_TOKEN_SECRET, "POST")
    print(resp)
    print(content)

tweet("hello_world")
