import encoding_fix
import requests
import sys

"""
In this script, we are requesting the same data as in wikipedia1-1.py, but doing two new things:

1. We are 'parameterizing' our query (specifying each of the query components separately, and then concatenating them into the API endpoint right before we send our request.

2. We are using a 'while TRUE' loop to 'continue' our query—making multiple requests to retrieve MUCH more data than we did before.
"""
# raw string:
# ?action=query&prop=revisions&titles=Python_(programming_language)&rvlimit=100&rvprop=timestamp|user&format=json')

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Game of Thrones',
              'rvlimit' : 20,
              'rvprop' : "timestamp|userid",
              'format' : 'json',
              'continue' : ''}

# /w/api.php?action=query&format=json&prop=revisions&list=&titles=Game+of+Thrones&rvprop=timestamp%7Cuser%7Cuserid&rvlimit=20&rvstart=2008-12-15T21%3A57%3A16.000Z&rvdir=newer

OUTPUT_FILE = "tvgot.tsv"
with open(OUTPUT_FILE, "w") as ofile:
    while True:
        wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
        response = wp_call.json()
        #print(parameters)
        #print(response)

        for page_id in response["query"]["pages"].keys():
            page_title = response["query"]["pages"][page_id]["title"]
            revisions = response["query"]["pages"][page_id]["revisions"]

            for rev in revisions:
                print(page_title + "\t" + str(rev["userid"]) + "\t" + rev["timestamp"])
                #if rev["user"] == '\u03a3':
                #    rev["user"] = "missing"
                ofile.write(page_title + "\t" + str(rev["userid"]) + "\t" + rev["timestamp"] + "\n")

                #ofile.write(str(i) + "\t" + n[0] + "\t" + n[1] + "\n")

        if 'continue' in response:
            parameters.update(response['continue'])
        else:
            break

print("Done")
