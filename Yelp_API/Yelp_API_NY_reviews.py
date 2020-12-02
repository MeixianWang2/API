import requests
import json
import pandas as pd
api_key='1TJnLOeAx6pkSBvcxy7QKEakp_YKcUzRfiKjOSxesn2T93uHj2JAoDll0kGwUTS1Z8PSz7SxEolSj2vhFnwzWCCxlayE0SKITuxCTWIHCwDjN4pXkUZgTSHEDfKOX3Yx'
headers = {'Authorization': 'Bearer %s' % api_key}

businesses = pd.read_csv('yelp/NY_business.csv',usecols=['business_id'])

a = businesses.business_id.tolist()
print(type(a))
for business in a:
    print(business)
    id = business

    url="https://api.yelp.com/v3/businesses/" + id + "/reviews"


    req = requests.get(url, headers=headers)

    parsed = json.loads(req.text)

    reviews = parsed["reviews"]
    with open('yelp/NY_reviews.json', 'a') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)
    
    print("--- Reviews ---")
    for review in reviews:
        print("User:", review["user"]["name"], "Rating:", review["rating"], "Review:", review["text"], "\n")
