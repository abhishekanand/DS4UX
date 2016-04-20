"""
How many people walked northbound on the BGT between 6 and 7 AM on August 28, 2014?
"""

import bgt_traffic

#print(bgt_traffic.traffic['03/31/2016']['06:00:00 AM']['ped nb'])

print(bgt_traffic.traffic['03/31/2016'])

sum = 0 ;
april_1 = bgt_traffic.traffic.get('03/31/2016')
for h_key, h_val in april_1.items():
    print (h_val['total'])
    sum += h_val['total']
print (sum)
