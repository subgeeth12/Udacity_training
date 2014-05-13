#!/usr/bin/env python

import sys
import re
import csv
     
# input comes from STDIN (standard input)
reader = csv.reader(sys.stdin ,delimiter='\t')

all_data =  list(reader)
tagDataList=[]
d= 0
c = 0

for line in all_data:
    if line[1]=="id":  ###----- output will only contain top 10 tags from question, answers, comments---###
        continue
 
    i = 0
    
    tagData= line[2].split(" ")
   

    for i in range(len(tagData)):
        if len(tagData[i]) == 0:
           continue

        print "%s\t%s" % (tagData[i], 1) 




