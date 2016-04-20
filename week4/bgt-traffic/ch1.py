"""
1. What day between January 1, 2014 and March 31, 2016 saw the most total traffic on the Burke-Gilman trail?

Data Format
Date,BGT North of NE 70th Total,Ped South,Ped North,Bike North,Bike South
03/31/2016 11:00:00 PM,2,0,1,1,0

"""
import bgt_traffic

april_1 = bgt_traffic.traffic.get('04/01/2015')
print (bgt_traffic.traffic)

"""
SOLUTION
"""
most_trafficdate = []  # Placeholder for most date
total_trsffic = 0 ; # intializing 
for date, data in bgt_traffic.traffic.items():  # Getting all first Level Key - in this case dates
    sum = 0 ; # intiating variable
    current_date = bgt_traffic.traffic.get(date) # Getting whole value set for give key
    for h_key, h_val in current_date.items(): # its nested
        #print (h_val['total'])
        sum += h_val['total']
    print(date ,":", sum )
