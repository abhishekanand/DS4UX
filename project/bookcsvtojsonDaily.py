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
bookdaily = {}
for revision in bookrevisions:
    day = revision['timestamp'][0:10]
    if day in bookdaily.keys():
        bookdaily[day] += 1
    else:
        bookdaily[day] = {}
        bookdaily[day] = 1

print(json.dumps(bookdaily, indent = 4 ))
