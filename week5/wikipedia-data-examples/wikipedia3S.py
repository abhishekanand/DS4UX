"""
What articles are in the category "Programming Languages created in 1991"?
Category page here: https://en.wikipedia.org/wiki/Category:Programming_languages_created_in_1991
Documentation here: https://www.mediawiki.org/wiki/API:Categorymembers
"""


import encoding_fix
import requests

parameters = {'action' : 'query',
              'prop' : 'categories',
              'titles' : 'Python (programming language)',
              'format' : 'json'}

parameters1 = {'action' : 'query',
              'prop' : 'categories',
              'titles' : 'Python (genus)',
              'format' : 'json'}

print("==============Python (programming language)============= ")
wp_call = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)
response = wp_call.json()
#print(response)
for page in response['query']['pages']['23862']['categories']:
    print(page['title'])

print("==============Python (genus)============= ")
wp_call1 = requests.get('http://en.wikipedia.org/w/api.php', params=parameters1)
response1 = wp_call1.json()
#print(response)
for page in response1['query']['pages']['4920126']['categories']:
    print(page['title'])
