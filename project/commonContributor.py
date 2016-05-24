# CSV to JSON

import csv
import json
from collections import Counter


bookFin = open('bookdata.json', "r")
bookrevisions = json.load(bookFin)
#print(json.dumps(revisions, indent = 4 ))

tvFin = open('tvdata.json', "r")
tvrevisions = json.load(tvFin)

# ===========
commonContributor = []
for revision in bookrevisions:
    bookuserid = revision['userid']
    for tvrevision in tvrevisions:
        tvuserid = tvrevision['userid']
        if bookuserid == tvuserid and bookuserid != '0' and tvuserid != '0':
            commonContributor.append(bookuserid)


# http://stackoverflow.com/a/5829377
print (Counter(commonContributor))
stats = (Counter(commonContributor))

# Counter(z).most_common(n) will list elements and counts as tuples in decreasing order, where n is the number of elements to list. Omit n to list everything.
# print (Counter(userlist).most_common())

# http://stackoverflow.com/a/280156
#  Which editor has made the total most edits to the article Panama Papers so far?
#print((max(stats, key=stats.get)) + 'editor has made the total ' + str(stats.get(max(stats, key=stats.get)))+'  edits which is the highest for the article Panama Papers so far')
