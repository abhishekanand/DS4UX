import bgt_traffic
import json

dict_temp = bgt_traffic.traffic

#getDayToll: Get daily toll 
#Input parameters: a string of a date (e.g., "06/30/2014")
#Return value: an int (e.g., 3234)
#Dependency: bgt_traffic
def getDayToll(date):
	times = dict_temp[date].keys()
	day_toll = 0
	for time in times:
		day_toll += dict_temp[date][time]["total"]
	return day_toll

#writeMonthToll: save a csv file that has every daily toll for a given month
#Input parameters: a string of month and a string of year (e.g., "06", "2014")
#Return value: None
#Dependency: bgt_traffic, getDayToll
def writeMonthToll(month, year):
	#1-2. Write a file
	fout = open(month+"-"+year+".csv", "w")
	fout.write("date, toll\n")
	# See how many of dates are there in a given month
	for date in dict_temp.keys():
		if date.split("/")[0] == month and date.split("/")[2] == year:
			fout.write(date + "," + str(getDayToll(date)) + "\n")
	fout.close()

#getMonthToll: Get monthly toll
#Input parameters: a string of month and a string of year (e.g., "06", "2014")
#Return value: an int (e.g., 73281)
#Dependency: bgt_traffic, getDayToll
def getMonthToll(month, year):

#writeYearToll: save a csv file that has every monthly toll for a given year
#Input parameters: a string of an year (e.g., "2014")
#Return value: None
#Dependency: bgt_traffic, getMonthToll
def writeYearToll(year):