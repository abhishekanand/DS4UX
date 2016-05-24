import encoding_fix
import operator
import requests
import json

show_titles = ["Unforgettable_(2011_TV_series)", "Angel_from_Hell","Austin_&_Ally", "Lab_Rats_(U.S._TV_series)","Melissa_Harris-Perry_(TV_series)", "Gravity_Falls", "MythBusters", "Of_Kings_and_Prophets", "American_Idol","Togetherness_(TV_series)", "Childrens_Hospital","Monopoly_Millionaires'_Club_(U.S._game_show)", "The_Good_Wife", "Mike_&_Molly","Banshee_(TV_series)","Littlest_Pet_Shop_(2012_TV_series)", "The_Soul_Man", "Person_of_Interest_(TV_series)", "Wander_Over_Yonder", "Beauty_&_the_Beast_(2012_TV_series)", "Crazy_Talk_(TV_series)", "FABLife", "The_Meredith_Vieira_Show", "The_Leftovers_(TV_series)"
]


ENDPOINT = 'https://en.wikipedia.org/w/api.php'

shows = {}

for t in show_titles:
	parameters = {'action' : 'query',
		'prop' : 'revisions', 
		'titles' : t,
		'rvlimit' : 500,
		'rvprop' : "ids", 
		'format' : 'json',
		'continue' : ''
	}

	revisions = 0
	while True:
		wp_call = requests.get(ENDPOINT, params=parameters)
		response = wp_call.json()
		pages = response['query']['pages']
		for page_id in pages:
			page = pages[page_id]
			page_revs = page['revisions']
			for rev in page_revs:
				revisions += 1
		if 'continue' in response:
			parameters.update(response['continue'])
		else:
			break
	result = {}
	result[t] = revisions
	shows.update(result)

fout = open("tv_show_2016.csv", "w")
fout.write("title,revisions\n")
for skey, sval in shows.items():
    fout.write(skey + "," + str(sval) + "\n")
fout.close()

#make a sorted version of our dictionary, with the most-edited show first
shows_sorted_max = sorted(shows.items(), key=operator.itemgetter(1), reverse = True)
max_rev = shows_sorted_max[0]
print("%s has the most (%d) revisions in the dataset" % (max_rev[0], max_rev[1]))

#make a sorted version of our dictionary, with the least-edited show first
shows_sorted_min = sorted(shows.items(), key=operator.itemgetter(1), reverse = False)
min_rev = shows_sorted_min[0]
print("%s has the fewest (%d) revisions in the dataset" % (min_rev[0], min_rev[1]))