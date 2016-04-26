"""
Instructor:Jonathan Morgan TA:Sungsoo Ray Hong
Contact: jmo25@uw.edu, rayhong@uw.edu
Office Hours:   
    Thursdays 5:00pm-5:50pm, 
    Student Lounge
Grade:
    95%: 3.8, 90%: 3.6, 85%: 3.3, 80%: 3.0, 75%: 2.5, 70%: 2.0"""

jDict = {
    "Instructor": "Jonathan Morgan",
    "TA": "Sungsoo Ray Hong",
    "Contact": ["jmo25@uw.edu", "rayhong@uw.edu"],
    "Office Hours": {
        "Time": "Thur. 5:00 p.m. ~ 5:50 p.m.",
        "Place": "Student Lounge"
    },
    "Grade": {
        "95%" : "3.8",
        "90%" : "3.6",
        "85%" : "3.3",
        "80%" : "3.0",
        "75%" : "2.5",
        "70%" : "2.0"
    }
 }

import json

#fout = open("jsonoutput.txt", "w")
#json.dump(jDict, fout, indent=4)
#fout.close()

#fin = open("jsonoutput.txt", "r")
#jsDict = json.load(fin)
#print json.dumps(jsDict, indent = 4)
#fin.close()