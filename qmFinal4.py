#!/usr/bin/env python

import sys
import csv
     
reader = csv.reader(sys.stdin ,delimiter='\t')

all_data =  list(reader)

for line in all_data:
    if line[0] == "id":
       continue
        
    if line [5] == "question":
       
    #-------------------------------------------------------------------------#
    #         Print Node ID and the corresponding authorID                    #
    #-------------------------------------------------------------------------#
       
       print "%s\t%s" % ( line[0],line[3])
    if line [5] <> "question":
    #-------------------------------------------------------------------------#
    #         Print Parent Node ID and the corresponding authorID              #
    #-------------------------------------------------------------------------#
       print "%s\t%s" % ( line[7], line[3] )

