#!/usr/bin/env python

import sys
import csv

time =[]
#----------------------------------------#
# input comes from STDIN (standard input)#
#----------------------------------------#

reader = csv.reader(sys.stdin ,delimiter='\t') 
all_data =  list(reader) # converting it into list

for line in all_data: 
    if line[0] == "id":
       continue
    time = line[8]  
    #------------------------------------------#
    # Get the authorID and the hour they posted#
    #------------------------------------------#

    print "%s\t%s" % ( line[3], time[11:13]) 
