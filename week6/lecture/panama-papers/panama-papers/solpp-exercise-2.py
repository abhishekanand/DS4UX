# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE


# https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Panama_Papers&rvdir=%20newer&rvprop=timestamp&rvdir=newer (For oldest 10)


#        2. How many edits per day did Panama Papers receive, on average, in its first two weeks?

import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               #'rvprop' : 'tags|timestamp|user',
               'rvdir' : 'newer',
               'rvlimit': 500,
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-04-17T17:59:05Z',
               'continue' : '' }

num_mobile_revisions = 0

done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for revision in revisions:
            num_mobile_revisions += 1


    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

print(parameters['titles'] + ' has had ' + str(num_mobile_revisions) + ' edits in first two weeks')
print(parameters['titles'] + ' has had ' + str(num_mobile_revisions/14) + ' edits on daily basis in first two weeks')
