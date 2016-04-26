import json
import csv
        
INPUT_FILE = "family.json"
OUTPUT_FILE = "family.csv"

with open(INPUT_FILE) as ifile:
    family_data = json.load(ifile)

#print the name of the first person in the 'people' list    
print(family_data['people'][0].get('name'))


with open(OUTPUT_FILE, "w") as ofile:
	writer=csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	writer.writerow(("name","type","age","favorite foods"))
	for k,v in family_data.items():
	    for i in v:
	        writer.writerow((i.get('name','unknown'),k,i.get('age','unknown'),', '.join(i.get('fav_foods',['unknown'])))) #note: using 'get' here since 'eva' doens't have a fav_food (intentionally left out)