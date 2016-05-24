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
tvdaily = {}
for revision in tvrevisions:
    day = revision['timestamp'][0:10]
    if day in tvdaily.keys():
        tvdaily[day] += 1
    else:
        tvdaily[day] = {}
        tvdaily[day] = 1

print(json.dumps(tvdaily, indent = 4 ))
