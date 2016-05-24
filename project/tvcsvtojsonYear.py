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
tvyears = {}
for revision in tvrevisions:
    year = revision['timestamp'][0:4]
    if year in tvyears.keys():
        tvyears[year] += 1
    else:
        tvyears[year] = {}
        tvyears[year] = 1

print(json.dumps(tvyears, indent = 4 ))
