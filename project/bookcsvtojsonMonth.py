# CSV to JSON

import csv
import json

bookcsvfile = open('bookdata.csv', 'r')
bookjsonfile = open('bookdata.json', 'w')

reader = csv.DictReader(bookcsvfile)
out = json.dumps([row for row in reader])
bookjsonfile.write(out)


bookFin = open('bookdata.json', "r")
bookrevisions = json.load(bookFin)
#print(json.dumps(revisions, indent = 4 ))

# ===========
bookmonths = {}
for revision in bookrevisions:
    month = revision['timestamp'][0:7]
    if month in bookmonths.keys():
        bookmonths[month] += 1
    else:
        bookmonths[month] = {}
        bookmonths[month] = 1

print(json.dumps(bookmonths, indent = 4 ))
