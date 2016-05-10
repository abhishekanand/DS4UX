import encoding_fix
import requests
import json

tv_show_2016 = ["Austin_&_Ally", "Unforgettable_(2011_TV_series)", "Lab_Rats_(U.S._TV_series)", "Angel_from_Hell", 
	"Melissa_Harris-Perry_(TV_series)", "Gravity_Falls", "MythBusters", "Of_Kings_and_Prophets", "American_Idol",
	"Togetherness_(TV_series)", "Childrens_Hospital", "Monopoly_Millionaires'_Club_(U.S._game_show)", "The_Good_Wife", "Mike_&_Molly",
	"Banshee_(TV_series)", "Littlest_Pet_Shop_(2012_TV_series)", "The_Soul_Man", "Person_of_Interest_(TV_series)", "Wander_Over_Yonder",
	"Beauty_&_the_Beast_(2012_TV_series)", "Crazy_Talk_(TV_series)", "FABLife", "The_Meredith_Vieira_Show", "The_Leftovers_(TV_series)"
]

#getRevision
#Input: receives a string (Wikipedia Title)
#Output: returns a list of revisions. Each component has user, timestamp, and comment
def getRevisions(keyword):

	parameters = {'action' : 'query',
		'prop' : 'revisions', 
		'titles' : keyword,
		'rvlimit' : 100,
		'rvprop' : "timestamp|user|comment", 
		'format' : 'json',
		'continue' : ''
	}

	revisions = []
	iteration = 0

	while True:
		wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
		response = wp_call.json()

		#Step 1. gather 100 revisions
		temp_id = "".join(response["query"]["pages"].keys())
		#Step 2. Save the gathered revisions to revisions = []
		revisions.extend(response["query"]["pages"][temp_id]["revisions"])
		#Step 3. Optional - Report progress in console
		print(keyword + " " + str(iteration) + " finished.")
		iteration += 1

		if 'continue' in response:
			parameters.update(response['continue'])
		else:
			break
	#We should return a result vale in function
	result = {}
	result[keyword] = revisions
	return result

keyword = tv_show_2016[2]
result = getRevisions(keyword)
#print(json.dumps(result, indent= 4))
print(str(len(result[keyword])) + " edits are made in " + keyword)