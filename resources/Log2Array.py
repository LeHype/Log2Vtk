import numpy as np 
import csv
import os 
import sys

from resources.VariableClass import *

def isFirstEntryFloatTry(v):
    try:     i = float(v[0])
    except:  return False
    return True

def LogFileReader(path,filename,ElementConnectivities,NumberNodes,UniqueId,Components):

    if not os.path.isfile(path+filename+'.log'): 
            print ('Log file "%s" not found'%(filename))
            sys.exit(2)


    TimeIncrements = []
    UniqueVariables = []
    
    Logfile=list(csv.reader(open(path+filename+'.log', "r"), delimiter=','))


    CurrentTime=-1			# Only write to Array when new unique Time is reached		
    for Line in Logfile:
        if len(Line)!= 0:
            if Line[0] == ' Time =' and Line[1]!=CurrentTime:
                CurrentTime=Line[1]
                TimeIncrements.append(float(CurrentTime))
    

    for i in range(len(UniqueId)):
        UniqueVariables.append(Variable(UniqueId[i], NumberNodes, Components[i], len(TimeIncrements)))
    pass
    i =0
    CurrentTime=-1
    CurrentTimeIndex =-1
    CurrentElementIndex=-1
    CurrentUniqueIdIndex=-1
    CurrentNodes= []
    CurrentData=[]
    while(i<len(Logfile)):
        if len(Logfile[i])!= 0:
            if Logfile[i][0] == ' Time =':
                CurrentTime = float(Logfile[i][1])
                CurrentTimeIndex= TimeIncrements.index(CurrentTime)
                CurrentElementIndex = int(Logfile[i][3])-1
                CurrentNodes= ElementConnectivities[CurrentElementIndex]
                CurrentUniqueIdIndex=UniqueId.index(Logfile[i+1][1])
                CurrentNumberComponents=UniqueVariables[CurrentUniqueIdIndex].NumberComponents
                j=1
                while(isFirstEntryFloatTry(Logfile[i+j])):
                    CurrentData.append(float(Logfile[i+j]))
                    j=j+1


        i=i+1
    
    




