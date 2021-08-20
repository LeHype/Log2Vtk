import csv
import os 
import sys 
def isFirstEntryIntTry(v):
    try:     i = int(v[0])
    except:  return False
    return True


def NodesAndElementsFromInput(path,filename):

    
    if not os.path.isfile(path+filename+'.inp'): 
            print ('Input file "%s" not found'%(filename))
            sys.exit(2)
    InputFile=list(csv.reader(open(path+filename+'.inp', "r"), delimiter=',',quotechar="'"))
    NodeDefinitionsLine = -1
    ElementDefinitionsLine = -1
    NodalCoordinates=[]
    ElementConnectivities = []

    NodeDefinitionsIdentifier = '*node'
    ElementDefinitionIdentifier = '*element'


# Find the Lines where the nodal/element definitions are made. If multiple instances of the identifier are
#found the script stops
    for i in range(len(InputFile)):

        if len(InputFile[i]) != 0:

            if NodeDefinitionsIdentifier.lower() == InputFile[i][0].lower():
                if NodeDefinitionsLine != -1 :
                    print('Multiple node definitions found. Please modify the Input file to ')
                    print('only contain one model.')
                    sys.exit(2)
                NodeDefinitionsLine = int(i)
            
            if ElementDefinitionIdentifier.lower() == InputFile[i][0].lower():
                if ElementDefinitionsLine != -1 :
                    print('Multiple element definitions found. Please modify the Input file to ')
                    print('only contain one model.')
                    sys.exit(2)
        
                ElementDefinitionsLine = int(i)
    i = 1
    while(isFirstEntryIntTry(InputFile[NodeDefinitionsLine+i])):
        Node = []
        for u in range(1,len(InputFile[NodeDefinitionsLine+i])):
            Node.append(float(InputFile[NodeDefinitionsLine+i][u]))
         
        NodalCoordinates.append(Node)

        i = i+1
    
    i = 1
    while(isFirstEntryIntTry(InputFile[ElementDefinitionsLine+i])):
        Element = []
        for u in range(1,len(InputFile[ElementDefinitionsLine+i])):
            Element.append(int(InputFile[ElementDefinitionsLine+i][u]))
         
        ElementConnectivities.append(Element)

        i = i+1
    
    return len(NodalCoordinates),NodalCoordinates,len(ElementConnectivities),ElementConnectivities 



        
        