import pandas as pd
import numpy as np
import json
import csv

with open('yelp/NY_reviews.json', 'r') as file:
    data = file.read().replace('\n', '').replace('}{', '},{')
    response = '['+data +']'
reviews = json.loads(response)
print(reviews)
def inputdict4sql(item, item_name):
    try:
        tmpitem = item[item_name]
    except:
        tmpitem = 'null'
    return tmpitem


for review in reviews:
    try:
        items = review['reviews']
        total = review['total']
        print(items)
        print(total)
        for item in items:
            try:
                review_id = inputdict4sql(item, 'id')
                review_url = inputdict4sql(item, 'url')
                text = inputdict4sql(item, 'text')
                stars = inputdict4sql(item, 'rating')
                date = inputdict4sql(item, 'time_created')
                # user = inputdict4sql(item, 'user')
                # print(user)
                user_id = inputdict4sql(item['user'], 'id')
                print(user_id)

                t = [review_id, user_id, review_url, text, stars, date]
                print(t)
                columns = ['review_id', 'user_id', 'review_url', 'text', 'stars', 'date']
                with open('yelp/NY_reviews.csv', 'a', newline='\n') as f:
                    write = csv.writer(f)
                    write.writerow(t)
            except:
                print(1)
                continue
    except:
        print(2)
