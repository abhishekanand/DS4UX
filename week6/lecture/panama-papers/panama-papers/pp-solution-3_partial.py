# What hour in the first two weeks had the highest number of edits?

import requests
import json

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Panama_Papers',
               'format' : 'json',
               'rvdir' : 'newer',
               'rvstart': '2016-04-03T17:59:05Z',
               'rvend' : '2016-04-17T17:59:05Z',
               'rvlimit' : 500,
               'continue' : '' }

#create an empty dictionary that will hold our edit counts by day and by hour
days = {}
no_edit_in_hour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#while loop to keep grabbing revisions until we've got them all
done = False
while not done:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    pages = response['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        revisions = page['revisions']
        #for each revision, we will use string slicing to grab the day and the hour
        #from the timestamp, and save them as separate variables
        for rev in revisions:
            revday = rev['timestamp'][5:10]
            revhour = rev['timestamp'][11:13]
            #start adding individual days and hours to our dictionary 'day'.
            #have we seen any revisions from this day before?
            if revday in days.keys():
                #have we seen any revisions from this hour of this day before?
                #if so, increment the value for this hour, since we just saw another!
                if revhour in days[revday].keys():
                    days[revday][revhour] += 1
                #if not, create a dictionary inside this day for this hour, and give it
                #a value of 1, since we've seen one revision from this hour
                else:
                    days[revday][revhour] = 1
            else:
            #if we haven't seen any revisions from that day yet,
            #add that day as a new key in 'days', and add a key/value to THAT day's
            #dictionary for the hour of the revision we just found.
                days[revday] = {}
                days[revday][revhour] = 1

    if 'continue' in response:
        parameters['continue'] = response['continue']['continue']
        parameters['rvcontinue'] = response['continue']['rvcontinue']
    else:
        done = True

#print(json.dumps(days, indent=4))




#print(no_edit_in_hour)

#print(type(days))
print("start")
print(no_edit_in_hour)
count = 0
for day in days:#.items():
    hours = days[day]
    count += 1
    print(day, count)
    #print(no_edit_in_hour)
    #print(hours)
    #print(type(hours))
    for h_key, h_val in hours.items():
        if(h_key == "00"):
            no_edit_in_hour[0] += h_val
        elif(h_key == "01"):
            no_edit_in_hour[1] += h_val
        elif(h_key == "02"):
            no_edit_in_hour[2] += h_val
        elif(h_key == "03"):
            no_edit_in_hour[3] += h_val
        elif(h_key == "04"):
            no_edit_in_hour[4] += h_val
        elif(h_key == "05"):
            no_edit_in_hour[5] += h_val
        elif(h_key == "06"):
            no_edit_in_hour[6] += h_val
        elif(h_key == "07"):
            no_edit_in_hour[7] += h_val
        elif(h_key == "08"):
            no_edit_in_hour[8] += h_val
        elif(h_key == "09"):
            no_edit_in_hour[9] += h_val
        elif(h_key == "10"):
            no_edit_in_hour[10] += h_val
        elif(h_key == "11"):
            no_edit_in_hour[11] += h_val
        elif(h_key == "12"):
            no_edit_in_hour[12] += h_val
        elif(h_key == "13"):
            no_edit_in_hour[13] += h_val
        elif(h_key == "14"):
            no_edit_in_hour[14] += h_val
        elif(h_key == "15"):
            no_edit_in_hour[15] += h_val
        elif(h_key == "16"):
            no_edit_in_hour[16] += h_val
        elif(h_key == "17"):
            no_edit_in_hour[17] += h_val
        elif(h_key == "18"):
            no_edit_in_hour[18] += h_val
        elif(h_key == "19"):
            no_edit_in_hour[19] += h_val
        elif(h_key == "20"):
            no_edit_in_hour[20] += h_val
        elif(h_key == "21"):
            no_edit_in_hour[21] += h_val
        elif(h_key == "22"):
            no_edit_in_hour[22] += h_val
        elif(h_key == "23"):
            no_edit_in_hour[23] += h_val
        else:
            pass


    print(no_edit_in_hour)

print("Final")

print(no_edit_in_hour)

print(max(no_edit_in_hour), no_edit_in_hour.index(max(no_edit_in_hour)) )
