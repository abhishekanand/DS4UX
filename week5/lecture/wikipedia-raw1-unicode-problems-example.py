import json
import requests

# making API request
wp_call = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Matteo I Visconti&rvlimit=50&rvprop=timestamp|user&format=json')

# parsing response
response = wp_call.json()

# printing results nicely
# NOTE: produces Unicode errors on Windows, but works on Mac or Linux
for page_id in response["query"]["pages"].keys():
    page_title = response["query"]["pages"][page_id]["title"]
    revisions = response["query"]["pages"][page_id]["revisions"]

    for rev in revisions:
        print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])

