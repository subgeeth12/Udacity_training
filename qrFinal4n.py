#!/usr/bin/env python
import sys

import csv
thisNode = None


authorList = []

for line  in sys.stdin:
    data = line.strip().split("\t") 
    
    
    if len(data)== 2: 
        node, authorID = data 
    else:
        continue
   
    
    if thisNode <> node and thisNode:
        print thisNode,"\t",authorList
        authorList = []
        authorList.append(authorID)
        thisNode = node
    else:
        
        authorList.append(authorID)
        thisNode = node

print thisNode,"\t",authorList
