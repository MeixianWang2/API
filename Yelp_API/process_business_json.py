import pandas as pd
import numpy as np
import json
import csv

with open('yelp/NY_business.json', 'r') as file:
    data = file.read().replace('\n', '').replace('}{', '},{')
    response = '['+data +']'
businesses = json.loads(response)
def inputdict4sql(item, item_name):
    try:
        tmpitem = item[item_name]
    except:
        tmpitem = 'null'
    return tmpitem
for business in businesses:
    try:
        items = business['businesses']
        print(items)
        for item in items:
            try:
                business_id = inputdict4sql(item, 'id')
                name = inputdict4sql(item, 'name')
                item_url = inputdict4sql(item, 'url')
                review_count = inputdict4sql(item, 'review_count')
                stars = inputdict4sql(item, 'rating')

                latitude = inputdict4sql(item['coordinates'], 'latitude')
                longitude = inputdict4sql(item['coordinates'], 'longitude')

                address = inputdict4sql(item['location'], 'display_address')
                city = inputdict4sql(item['location'], 'city')
                state = inputdict4sql(item['location'], 'state')
                postal_code = inputdict4sql(item['location'], 'zip_code')

                categories = inputdict4sql(item, 'categories')

                t = [business_id, name, item_url, review_count, stars, latitude, longitude,
                     address, city, state, postal_code, categories]
                print(t)
                columns = ['business_id', 'name', 'website', 'review_count', 'stars', 'latitude',
                           'longitude', 'address', 'city', 'state', 'postal_code', 'categories']
                with open('NY_business.csv', 'a',newline='\n') as f:
                    # using csv.writer method from CSV package
                    write = csv.writer(f)
                    write.writerow(t)

            except:
                print(1)
                continue
    except:
        print(2)



