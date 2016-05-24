import encoding_fix
import operator
import requests
import json

show_titles = ["Unforgettable_(2011_TV_series)", "Angel_from_Hell","Austin_&_Ally", "Lab_Rats_(U.S._TV_series)","Melissa_Harris-Perry_(TV_series)", "Gravity_Falls", "MythBusters", "Of_Kings_and_Prophets", "American_Idol","Togetherness_(TV_series)", "Childrens_Hospital","Monopoly_Millionaires'_Club_(U.S._game_show)", "The_Good_Wife", "Mike_&_Molly","Banshee_(TV_series)","Littlest_Pet_Shop_(2012_TV_series)", "The_Soul_Man", "Person_of_Interest_(TV_series)", "Wander_Over_Yonder", "Beauty_&_the_Beast_(2012_TV_series)", "Crazy_Talk_(TV_series)", "FABLife", "The_Meredith_Vieira_Show", "The_Leftovers_(TV_series)"
]


def getRevisions(show_title):
    """
    Input: receives a string (Wikipedia page title)
    Output: returns a dict with the title and the number of revisions
    """
    ENDPOINT = 'https://en.wikipedia.org/w/api.php'
    parameters = {'action' : 'query',
        'prop' : 'revisions', 
        'titles' : show_title,
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
    result[show_title] = revisions
    return result

def saveResults(show_dict, fname):
    """
    Input: a dictionary of show titles and revision counts, and a filename
    Output: a CSV of titles and counts with the specified filename
    """
    fout = open(fname, "w")
    fout.write("title,revisions\n")
    for skey, sval in show_dict.items():
        fout.write(skey + "," + str(sval) + "\n")
    fout.close()

def findExtremeValue(show_dict, max=True):
    """
    Input: 
        * a dictionary with strings keys and int values
        * a flag for returning max (default) or min val
    Output: item with the max (or min) value in the dictionary
    """
    shows_sorted = sorted(show_dict.items(), key=operator.itemgetter(1), reverse = max)
    return shows_sorted[0]

### MAIN METHOD BEGINS HERE ####
shows = {}
for t in show_titles:
    show = getRevisions(t)
    shows.update(show)

saveResults(shows, "tv_show_2016.csv")

max_rev = findExtremeValue(shows, max=True)
print("%s has the most (%d) revisions in the dataset" % (max_rev[0], max_rev[1]))

min_rev = findExtremeValue(shows, max=False)
print("%s has the fewest (%d) revisions in the dataset" % (min_rev[0], min_rev[1]))