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
bookyears = {}
for revision in bookrevisions:
    year = revision['timestamp'][0:4]
    if year in bookyears.keys():
        bookyears[year] += 1
    else:
        bookyears[year] = {}
        bookyears[year] = 1

print(json.dumps(bookyears, indent = 4 ))
