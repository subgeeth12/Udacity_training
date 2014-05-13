#!/usr/bin/env python
import sys

import csv

listHour=[]
from collections import defaultdict
from operator import itemgetter
thisAuthorID = None


for line  in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
       authorID, hour = data
       hour = int(hour)
       
    else:
        continue
    
    if (thisAuthorID == authorID) or (thisAuthorID == None):                                                           
         listHour.append(hour)
         thisAuthorID = authorID
         
    else:
        if thisAuthorID <> authorID and thisAuthorID:  
           
           counter = {}
             
           
               #-------------------------------------------------#
               #Loop through the list of hours for each authorID-#
               #-------------------------------------------------#
             
           for k in listHour:
               #------------------------------------#
               #Identify the occurrence of each hour#
               #------------------------------------#
               counter[k] = listHour.count(k)

            #-----------------------------------------------------------------#
            #  Identify the hour in which author posted the maximum post      #
            #-----------------------------------------------------------------#

           list1 = [key for key,val in counter.iteritems() if val == max(counter.values())]
           
           for item in list1:
               print "%s\t%s"% (thisAuthorID,item)
           listHour = []
           thisAuthorID = authorID
           listHour.append(hour)

#----------------------------------------#
#print the hour in which the user posted #
#----------------------------------------#

counter = {}
for k in listHour:
    counter[k] = listHour.count(k)
list1 = [key for key,val in counter.iteritems() if val == max(counter.values())]

for item in list1:
    print "%s\t%s"% (thisAuthorID,item)
           

