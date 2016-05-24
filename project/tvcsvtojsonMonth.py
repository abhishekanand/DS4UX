# CSV to JSON

import csv
import json

tvcsvfile = open('tvdata.csv', 'r')
tvjsonfile = open('tvdata.json', 'w')

reader = csv.DictReader(tvcsvfile)
out = json.dumps([row for row in reader])
tvjsonfile.write(out)


tvFin = open('tvdata.json', "r")
tvrevisions = json.load(tvFin)
#print(json.dumps(revisions, indent = 4 ))

# ===========
tvmonths = {}
for revision in tvrevisions:
    month = revision['timestamp'][0:7]
    if month in tvmonths.keys():
        tvmonths[month] += 1
    else:
        tvmonths[month] = {}
        tvmonths[month] = 1

print(json.dumps(tvmonths, indent = 4 ))
