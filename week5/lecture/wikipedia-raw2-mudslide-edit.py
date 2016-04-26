import json
import requests

url_base = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%s&rvlimit=500&rvprop=size|comment|tags|timestamp|user&format=json'

page = "2011 Tōhoku earthquake and tsunami"

wp_call = requests.get(url_base % (page))
response = wp_call.json()

for page_id in response["query"]["pages"].keys():
    page_title = response["query"]["pages"][page_id]["title"]
    revisions = response["query"]["pages"][page_id]["revisions"]

    # we only want to print information associated with the revisions 
    # tagged with "mobile edit"
    for rev in revisions:
        if "mobile edit" in rev["tags"]:
            print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"] +
                  "\t" + str(rev["size"]))
