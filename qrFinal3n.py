#!/usr/bin/env python
import sys
import re
import csv
import heapq
import collections 
import operator

thisTagName = None
thisCounter = 0
dict1 = {}
dict2 = {}

for line  in sys.stdin:
    data = line.strip().split('\t')
    if len(data)== 2:

       tagNames, counts= data
    else:
        continue
    
   
    if thisTagName <> tagNames and thisTagName <> None:
       dict1[thisTagName] = thisCounter
       thisCounter= 0
    thisTagName = tagNames
    counts = int(counts)  
    thisCounter = thisCounter + 1
dict1[thisTagName] = thisCounter
     
    
#---------------------------------------------------#
#sort the dictionary to get the maximum of 10 values#
#---------------------------------------------------#

dict1= dict(sorted(dict1.iteritems(),key =operator.itemgetter(1),reverse= True)[:10])


for key, value in dict1.iteritems():
    print "%s\t%d" % (key,value)
