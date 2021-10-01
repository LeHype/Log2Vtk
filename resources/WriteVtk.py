import csv 
import os 
import glob
import numpy as np
def WriteVtk(path, filename, UniqueVariables,UniqueId, NumberElements, ElementConnectivities, NumberNodes, NodalCoordinates,Deformation,UniqueElementId ):
    VtuFilesinFolder = glob.glob(path+'/*vtu')
    for File in VtuFilesinFolder:
        os.remove(File)
    ElementConnectivities = np.array(ElementConnectivities)-1
    #ElementConnectivities = [[x-1 for y in ElementConnectivities]  for x in y]
    for j in range(len(UniqueVariables[0].TimeIncrements)):
        if Deformation.lower() == 'yes':
            NodalCoordinatesChanged = NodalCoordinates
            for i in range(len(NodalCoordinates)):
                for k in range(len(NodalCoordinates[0])):
                    NodalCoordinatesChanged[i][k] = NodalCoordinates[i][k] + UniqueVariables[UniqueId.index('U')].Data[j][i][k]
        else:
            NodalCoordinatesChanged=NodalCoordinates
        VTUPRINT =[]
        VTUPRINT.append(['<VTKFile', 'type="UnstructuredGrid"', 'version="0.1"', 'byte_order="LittleEndian">'])
        VTUPRINT.append(['<UnstructuredGrid>'])
        VTUPRINT.append(['<Piece', 'NumberOfPoints="'+str(NumberNodes)+'"', 'NumberOfCells="'+str(NumberElements)+'">'])
        VTUPRINT.append(['<Points>'])
        VTUPRINT.append(['<DataArray', 'type="Float64"', 'NumberOfComponents="3"', 'format="ascii">'])
        for i in range(NumberNodes):
            VTUPRINT.append(NodalCoordinatesChanged[i])
        VTUPRINT.append(['</DataArray>'])
        VTUPRINT.append(['</Points>'])
        UniqueIdString = ''
        for u in range(len(UniqueVariables)):
            if u != len(UniqueVariables)-1:
                UniqueIdString = UniqueIdString+str(UniqueVariables[u].UniqueId)+','
            else:
                UniqueIdString = UniqueIdString+str(UniqueVariables[u].UniqueId)

        VTUPRINT.append(['<PointData', 'Scalars="'+UniqueIdString+'">'])
        for Var in UniqueVariables:

            VTUPRINT.append(['<DataArray', 'type="Float32"', 'Name="'+str(Var.UniqueId)+'"', 'NumberOfComponents="'+str(Var.NumberComponents)+'"', 'format="ascii">'])
            for i in range(NumberNodes):
                VTUPRINT.append(Var.Data[j][i])
            VTUPRINT.append(['</DataArray>'])
        VTUPRINT.append(['</PointData>'])

        VTUPRINT.append(['<Cells>'])
        VTUPRINT.append(['<DataArray', 'type="Int32"', 'Name="connectivity"', 'format="ascii">'])
        for i in range(NumberElements):
            
            VTUPRINT.append(ElementConnectivities[i])
        VTUPRINT.append(['</DataArray>'])
        VTUPRINT.append(['<DataArray', 'type="Int32"', 'Name="offsets"', 'format="ascii">'])
        for i in range(NumberElements):
            VTUPRINT.append([str(len(ElementConnectivities[0])*(i+1))])
        VTUPRINT.append(['</DataArray>'])
        VTUPRINT.append(['<DataArray', 'type="UInt8"', 'Name="types"', 'format="ascii">'])
        for i in range(NumberElements):
            VTUPRINT.append([str(UniqueElementId)])
        VTUPRINT.append(['</DataArray>'])
        VTUPRINT.append(['</Cells>'])
        VTUPRINT.append(['</Piece>'])
        VTUPRINT.append(['</UnstructuredGrid>'])
        VTUPRINT.append(['</VTKFile>'])
        file_object_w = open(path+'/Heat_transfer_'+str((j))+'.vtu','w')
        NewVTU = csv.writer(file_object_w, delimiter=' ',quotechar="'")
        for k in range(len(VTUPRINT)):
            NewVTU.writerow(VTUPRINT[k])
        file_object_w.close()
