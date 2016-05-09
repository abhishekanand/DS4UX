# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# Exercise 4:
# How many other articles has User:Czar edited on Wikipedia since they created Panama Papers?
import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvprop' : 'userid|timestamp|user',
               'rvdir' : 'newer',
               'rvlimit': 500,
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-04-17T17:59:05Z',

               'continue' : '' }

count =0
done = False
solution = {}


while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()


    # print(json.dumps(response, indent =4))
    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for revision in revisions:
            count += 1
            #print(revision)
            #print(revision['timestamp']
            #print(revision['timestamp'][11:13])
            hour = revision['timestamp'][11:13]
            if hour in solution.keys():
                for users_dict in solution[hour]:
                    if revision['userid'] in users_dict.keys():
                        #print(users_dict[revision['userid']])
                        users_dict[revision['userid']] = users_dict[revision['userid']]+1
                        #print(users_dict[revision['userid']])
                    else:
                        users_dict[revision['userid']]=1
                #print(users_dict)
            else:
                data = []
                data.append({revision['userid']:1})
                solution[hour]=data


            #print("----------------")
            # for rev in revision:
            #     print(rev)


    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

print(json.dumps(solution, indent =4))
print(count)
