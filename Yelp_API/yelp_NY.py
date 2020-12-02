import requests
import json
api_key='1TJnLOeAx6pkSBvcxy7QKEakp_YKcUzRfiKjOSxesn2T93uHj2JAoDll0kGwUTS1Z8PSz7SxEolSj2vhFnwzWCCxlayE0SKITuxCTWIHCwDjN4pXkUZgTSHEDfKOX3Yx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'

# In the dictionary, term can take values like food, cafes or businesses like McDonalds
params = {'term': 'restaurant', 'location': 'New York City'}

# Making a get request to the API
req = requests.get(url, params=params, headers=headers)

# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# printing the text from the response
print(json.loads(req.text))