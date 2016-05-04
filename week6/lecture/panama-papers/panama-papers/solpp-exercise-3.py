# Copyright (C) 2016 Ben Lewis, Morten Wang, and Jonathan Morgan
# Licensed under the MIT license, see ../LICENSE

# 2. How many edits has Panama Papers receive from mobile devices in since it was created?

# https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Panama_Papers&rvdir=%20newer&rvprop=timestamp&rvdir=newer (For oldest 10)

import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

# parameters = { 'action' : 'query',
#                'prop' : 'revisions',
#                'titles' : 'Panama Papers',
#                'format' : 'json',
#                #'rvprop' : 'tags|timestamp|user',
#                'rvdir' : 'newer',
#                'rvlimit': 5,
#                'rvstart': '2016-04-03T17:59:05Z',
#                'rvend' : '2016-04-03T18:59:05Z',
#                'continue' : '' }

num_revisions = 0

done = False
while not done:

    parameters = { 'action' : 'query',
                   'prop' : 'revisions',
                   'titles' : 'Panama Papers',
                   'format' : 'json',
                   #'rvprop' : 'tags|timestamp|user',
                   'rvdir' : 'newer',
                   'rvlimit': 5,
                   'rvstart': '2016-04-03T17:59:05Z',
                   'rvend' : '2016-04-03T18:59:05Z',
                   'continue' : '' }


    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()
    print(json.dumps(response, indent = 4))

    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for revision in revisions:
            num_revisions += 1
            #print(json.dumps(revision, indent = 4))
            print('\n\n\n')


    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
        parameters['rvend'] = response['rvend']['2016-04-03T20:59:05Z']
    else:
        done = True

print(parameters['titles'] + ' has had ' + str(num_revisions) + ' edits in first two weeks')
