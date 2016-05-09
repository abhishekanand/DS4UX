# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# How many views did Panama Papers have in the first week?
# What proportion of those views came from devices using the mobile web browser?
# documentation https://wikimedia.org/api/rest_v1/?doc

import requests
from urllib.parse import quote
import json
from datetime import datetime
import calendar

ENDPOINT = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

highestview = 0
viewdate = "test"
#first, we gather the total views from all devices....
wp_code = 'en.wikipedia'
access = 'all-access'
agents = 'all-agents'
page_title = 'Panama Papers'
period = 'daily'
start_date = '20160403'
end_date = '20160417'

wp_call = requests.get(ENDPOINT + wp_code + '/' + access + '/' + agents + '/' + quote(page_title, safe='') + '/' + period + '/' + start_date + '/' + end_date)
responses = wp_call.json()

# print(response)
print(json.dumps(responses, indent = 4))
print(type(responses))
#print(max(response, key=responses.get))
print("--------------------------------")



for i,day in enumerate(responses['items']):
#     print(response['items'][i])
    if (highestview < responses['items'][i]['views']):
        highestview = responses['items'][i]['views']
        viewdate = responses['items'][i]['timestamp']

print(highestview)
print(viewdate)

# http://stackoverflow.com/a/29519293
oldformat = viewdate[0:8]
print(oldformat)
datetimeobject = datetime.strptime(oldformat,'%Y%m%d')

print(calendar.day_name[datetimeobject.weekday()])
