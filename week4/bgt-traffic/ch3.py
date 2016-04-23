"""
3. How much southbound traffic does the Burke-Gilman get, on average, during Morning commute hours?
   How much does it get during evening commute hours?
Note: for this question, assume morning commute hours start at 7am and end at 10am, and that evening commute hours start at 4pm and end at 7pm.
    You can also consider these to be hours to be "commute hours" even on weekends, since our data doesn't contain days of the week.
"""

import bgt_traffic

datecount = 0
totalsb_morning = 0
totalsb_evening = 0

for date, data in bgt_traffic.traffic.items():  # Getting all first Level Key - in this case dates
    datecount += 1  # intiating variable
    current_date = bgt_traffic.traffic.get(date) # Getting whole value set for give key
    for h_key, h_val in current_date.items(): # its nested
        if(h_key == "07:00:00 AM" or h_key == "08:00:00 AM" or h_key == "09:00:00 AM"):
            totalsb_morning += h_val['bike sb']
            totalsb_morning += h_val['ped sb']
        if(h_key == "04:00:00 PM" or h_key == "05:00:00 PM" or h_key == "06:00:00 PM"):
            totalsb_evening += h_val['bike sb']
            totalsb_evening += h_val['ped sb']
print("DateCount :", datecount )
print ("Morning ", totalsb_morning ,":" ,totalsb_morning/datecount)
print ("evening ", totalsb_evening ,":" ,totalsb_evening/datecount)
