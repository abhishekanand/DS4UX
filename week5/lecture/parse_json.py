import json

json_string = """{
	"people" : [
	{ 
		"name" : "Jonathan",
		"age" : 34,
		"gender" : "male",
		"fav_foods" : ["pizza","pasta","ice cream"]
	},

	{ 
		"name" : "Dana",
		"age" : 28,
		"gender" : "female",
		"fav_foods" : ["pizza","steak","sour patch kids"]
		
	}

	],
	
	"animals" : [
	{ 
		"name" : "Portia",
		"age" : 10,
		"gender" : "female",
		"fav_foods" : ["kibble", "tuna"]
		
	},
		
	{ 
		"name" : "Eva",
		"age" : 5,
		"gender" : "female"		
	},

	{ 
		"name" : "Ozy",
		"age" : 2,
		"gender" : "male",
		"fav_foods" : ["steak", "carrion"]
		
	}
	]
}"""

# What type is json_string?
print("json_string's type is:")
print(type(json_string))

# Parsing the json, printing the dict, printing the type
parsed_json = json.loads(json_string)
print("parsed_json's type is:")
print(type(parsed_json))

# Looking inside the dict to print fish names
print("\nThe animals names are:")
for animal in parsed_json["animals"]:
    print(animal["name"])
