import oauth2 as oauth

CONSUMER_KEY = '2KdjuDkrAsgIFYN6ecIuQ'
CONSUMER_SECRET = 'd0bVvlsobfUGjoqqFrAFX98zkWNYGntiVPxnLiKO4'
ACCESS_TOKEN = '1864732598-QO0wi40n5JPPBVXiptoMCrrsTlgwqWHMe1SMIcZ'
ACCESS_TOKEN_SECRET = 'L2SFsTYHuhDtvQDZjzrbT8WhvpcWFHGRKi1ch8GwjQs'
URL = 'https://api.twitter.com/1.1/statuses/update.json'
BODY = '{"status": "hello!"}'

def oauth_req(url, key, secret, http_method="GET", body='', http_headers=None):
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=body, headers=http_headers)
    return content

print oauth_req(URL, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, "POST", BODY)
