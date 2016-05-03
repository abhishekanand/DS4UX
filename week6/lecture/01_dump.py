"""
dump / dumps example: Save revisions of every state of USA
"""
import encoding_fix
import requests
import json

states = ["Alabama"#, "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut"
	#, "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana"
	#, "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire"
	#, "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island"
	#, "South Carolina", "South Dakota", "Tennessee", "Texas" ,"Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
]

parameters ={
	'action': 'query',
	'prop':'revisions',
	'titles': 'Alabama',
	'rvprop':"timestamp|user|comment",
	'rvlimit': 10,
	'format':'json',
	'continue':''
}

wp_call = requests.get("https://en.wikipedia.org/w/api.php", params = parameters)
response = wp_call.json()

# print (json.dumps(response, indent =4))
print(json.dumps(response["query"]["pages"]["303"]["revisions"], indent = 4))
