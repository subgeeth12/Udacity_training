#!/usr/bin/env python
import sys
myAuthorID = None
Count = 0
answerLength = 0
questionlength = 0
trick= "true"
for line  in sys.stdin:
    data = line.strip().split("\t") 
    if len(data) == 3:
        authorID, length,nodeType= data
    else:
        continue
    
#-------------------------------------------------------------------------------#
#Skip the first line and if the previous authorID and current authorID are equal#
#-------------------------------------------------------------------------------#

    if myAuthorID <> authorID and myAuthorID <> None and trick =="False":
       if answerLength == 0 and questionlength <>0:
           print "%s\t%d\t%0.1f" %(myAuthorID, int(questionlength) , float(answerLength))
          
       if answerLength <>0 and questionlength<> 0:
           print "%s\t%d\t%0.1f" %(myAuthorID, int(questionlength) , float(answerLength)/Count) 
           answerLength = 0
           Count = 0
       trick ="true"
    
    if nodeType == "question":
        questionlength = length  # reading the question length
        myAuthorID = authorID
        trick="False" #---- this assignment is to help print the nodes which has question
    else:
 
        if nodeType <> "question": 
            
            if myAuthorID == authorID or myAuthorID == None:
               answerLength = int(length) + float(answerLength)
               Count = Count + 1
               myAuthorID = authorID
            else:
               
                answerLength =length
                Count = 1
                myAuthorID = authorID
            
            
#-------------------#
#print the last line#
#-------------------#


if answerLength == 0 and questionlength <>0 : 
    print "%s\t%d\t%0.1f" %(myAuthorID, int(questionlength) , float(answerLength))
if answerLength <> 0 and questionlength <> 0:
    print "%s\t%d\t%0.1f" %(myAuthorID, int(questionlength) , float(answerLength)/Count) 
