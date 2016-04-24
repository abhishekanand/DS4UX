"""
4. Write a program that generates a CSV file called march_2016_daily_ped_counts.csv of the daily north- and south-bound pedestrian counts for March 2016, in chronological order. Your file should contain column headers and it should be possible to open it in a spreadsheet program like Microsoft Excel or Google Sheets.
"""


import bgt_traffic
import time

# http://stackoverflow.com/questions/8142364/how-to-compare-two-dates
# http://stackoverflow.com/a/31544886
startdate = "03/01/2016"
enddate = "03/31/2016"

startdate1 = time.strptime(startdate, "%m/%d/%Y")
enddate2 = time.strptime(enddate, "%m/%d/%Y")
count = 0
date_list = [];
 # Getting all first Level Key - in this case dates
for date, data in bgt_traffic.traffic.items():
    actualdate = time.strptime(date, "%m/%d/%Y")
    if (startdate1 <= actualdate <= enddate2 ):
        date_list.append(date)
        date_list.sort()
        #print(date_list)

index =0 ;

for dates in date_list:
    for date, data in bgt_traffic.traffic.items():
        total_ped_nb = 0
        total_ped_sb = 0
        if date == date_list[index]:
            current_date = bgt_traffic.traffic.get(date) # Getting whole value set for give key
            for h_key, h_val in current_date.items():
                total_ped_sb += h_val['ped sb']
                total_ped_nb += h_val['ped nb']
            print (date ,":", total_ped_sb, ":" ,total_ped_nb)
    index += 1
