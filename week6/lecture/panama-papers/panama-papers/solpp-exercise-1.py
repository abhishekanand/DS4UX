
# Copyright (C) 2016 Ben Lewis, Morten Wang, and Nathan TeGrotenhuis
# Licensed under the MIT license, see ../LICENSE
# How many edits did Panama Papers receive in its first 24 hours?

import requests
from collections import Counter  # http://stackoverflow.com/a/5829377

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvlimit': 'max',
               'continue' : '' }

num_revisions = 0
userlist = []
done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        for revision in revisions:
            num_revisions += 1
            userlist.append(revision['user'])

    #print('Done one query, num revisions is now ' + str(num_revisions))

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

print(parameters['titles'] + ' had ' + str(num_revisions) + ' revisions since article creation')
#print(len(userlist))

# http://stackoverflow.com/a/5829377
# print (Counter(userlist))
stats = (Counter(userlist))

# Counter(z).most_common(n) will list elements and counts as tuples in decreasing order, where n is the number of elements to list. Omit n to list everything.
# print (Counter(userlist).most_common())

# http://stackoverflow.com/a/280156
#  Which editor has made the total most edits to the article Panama Papers so far?
print((max(stats, key=stats.get)) + 'editor has made the total ' + str(stats.get(max(stats, key=stats.get)))+'  edits which is the highest for the article Panama Papers so far')
