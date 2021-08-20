import os
import sys 
def ReadConfig(filename):


    if not os.path.isfile(filename): 
            print ('Parameter file "%s" not found'%(filename))
            sys.exit(2)

    #read config file  
    odb2vtk = open(filename,'rt')
    read = odb2vtk.read()
    input = read.split("'")

    #Logfile and Input File Path
    LogPath = input[1]
    
    #Name of the simulation. This is the name of the input file.
    SimName = input[3]
    
    #Path for the Vtu Files to be stored
    VtuPath = input[5]

    #Dimension of Model
    Dimension = input[7]

    #Plot deformation ? 
    Deformation = input[9]

    #Array wih unique one character identifiers
    UniqueId = input[11].split(',')
    Components = input[13].split(',')
    for i in range(len(Components)):
            Components[i] = int(Components[i])
    return LogPath,SimName,VtuPath,UniqueId,Components