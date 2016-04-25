"""
2. What was the busiest hour of any day for northbound bike traffic? How about southbound pedestrian traffic?
"""


import bgt_traffic

"""
SOLUTION
"""
busiest_hour_nb_bike = []
nb_date = []
busiest_hour_sb_ped = []
sb_date = []  # Placeholder for most date
highest_nb_bike = 0
highest_sb_ped = 0  # initializing

for date, data in bgt_traffic.traffic.items():  # Getting all first Level Key - in this case dates
    current_date = bgt_traffic.traffic.get(date)  # Getting whole value set for give key
    for h_key, h_val in current_date.items():  # its nested
        if h_val['bike nb'] > highest_nb_bike:
            highest_nb_bike = h_val['bike nb']
            busiest_hour_nb_bike = h_key
            nb_date = date
        if h_val['ped sb'] > highest_sb_ped :
            highest_sb_ped = h_val['ped sb']
            busiest_hour_sb_ped = h_key
            sb_date = date

print('Bike North Bound :', nb_date, ':', busiest_hour_nb_bike, ':', highest_nb_bike)
print('Ped South Bound', sb_date, ":", busiest_hour_sb_ped, ":", highest_sb_ped)
