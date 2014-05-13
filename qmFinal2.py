#!/usr/bin/env python

import sys
import csv
Count = 0

#----------------------------------------#
# input comes from STDIN (standard input)#
#----------------------------------------#
reader = csv.reader(sys.stdin ,delimiter='\t')


all_data =  list(reader)

for line in all_data:
 
    if line[0] == "id":#--Skip First Line--#
       continue
    if line [5]== "question":
       #-------------------------------------------------------#
       # Get the nodeID, length of the post,and the nodeType   #
       #-------------------------------------------------------#
       print "%d\t%s\t%s" % ( int(line[0]), len(line[4]), line[5])
       Count = Count + 1
    if line [5] == "answer":
       #-----------------------------------------------------------#
       # Get the parentnodeID, length of the post,and the nodeType #
       #-----------------------------------------------------------#
       print "%d\t%s\t%s" % ( int(line[7]), len(line[4]), line[5])

