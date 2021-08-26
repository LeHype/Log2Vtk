import csv
import numpy as np

from tkinter import *
from resources.Gui import *
from resources.ConfigFile import *
from resources.InpFile2Array import *
from resources.VariableClass import *
from resources.Log2Array import *
from resources.WriteVtk import *
def main():

	path,filename,vtupath,UniqueId,Components,Deformation = ReadConfig('config.txt')

	NumberNodes,NodalCoordinates,NumberElements,ElementConnectivities = NodesAndElementsFromInput(path, filename)

	UniqueVariables = LogFileReader(path, filename, ElementConnectivities,NumberNodes,UniqueId,Components)

	WriteVtk(vtupath, filename, UniqueVariables,UniqueId, NumberElements, ElementConnectivities, NumberNodes, NodalCoordinates,Deformation)

	pass
if __name__=='__main__' :
	main()
	sys.exit(2)
pass
## Read input File 
for u in range(len(InputFile)):
	if InputFile[u] == ['*NODE']:
		Head = u+1
		break
Coordinates = np.zeros((NumberNodes,3))
for i in range(0,NumberNodes):
	Coordinates[i][0] = float(InputFile[Head+i][1])
	Coordinates[i][1] = float(InputFile[Head+i][2])
	Coordinates[i][2] = float(InputFile[Head+i][3])
ElemConnect = np.zeros((NumberElements,4))
for i in range(len(InputFile)):
	if InputFile[i] == ['*ELEMENT', 'TYPE=U1', 'ELSET=UEL']:
		Head = i+1
for i in range(0,NumberElements):
	ElemConnect[i][0] = int(InputFile[Head+i][1])-1
	ElemConnect[i][1] = int(InputFile[Head+i][2])-1
	ElemConnect[i][2] = int(InputFile[Head+i][3])-1
	ElemConnect[i][3] = int(InputFile[Head+i][4])-1

## Get Time steps 
TimeIncrements = []		# Array for each unique Timeincrement
Head = 0			# Readhead
CurrentTime=-1			# Only write to Array when new unique Time is reached		
for Line in Logfile:
	if len(Line)!= 0:
		if Line[0] == ' Time =' and Line[1]!=CurrentTime:
			CurrentTime=Line[1]
			TimeIncrements.append(float(CurrentTime))
Elemliste=[]
# for i in range(len(Logfile)):
# 	try:
# 		if float(Logfile[i][1])==TimeIncrements[0] and float(Logfile[i][0]==  ' Time =' ):
# 			K =	[[float(Logfile[i+2][1]),float(Logfile[i+2][2]),float(Logfile[i+2][3])],
# 			         [float(Logfile[i+3][1]),float(Logfile[i+3][2]),float(Logfile[i+3][3])],
# 				 [float(Logfile[i+4][1]),float(Logfile[i+4][2]),float(Logfile[i+4][3])],
# 				 [float(Logfile[i+5][1]),float(Logfile[i+5][2]),float(Logfile[i+5][3])]
# 			]
# 			Elemliste.append(K)
# 	except:
# 		pass

# TrueNodeCoords=[]
# for i in range(len(Vtu)):
# 	if Vtu[i] == ['<DataArray', 'type="Float64"', 'NumberOfComponents="3"', 'format="ascii">']:
# 		j=1
# 		while(True):
# 			print(i,j)
# 			if Vtu[i+j] ==  ['</DataArray>']:
# 				break
# 			TrueNodeCoords.append([float(Vtu[i+j][1]),float(Vtu[i+j][3]),float(Vtu[i+j][5])])
# 			j = j+1

# 		if i>200000:
# 			break
# print(len(TrueNodeCoords),'asdasdasd')
# Pointer =np.zeros((len(TrueNodeCoords),2))
# b =0
# print(len(TrueNodeCoords),'RRRRR')
# for i in range(len(TrueNodeCoords)):
# 	for j in range(len(Elemliste)):
# 		for k in range(4):
# 			if np.isclose(TrueNodeCoords[i][0],Elemliste[j][k][0],atol=1E-5) and np.isclose(TrueNodeCoords[i][1],Elemliste[j][k][1],atol=1E-5) and np.isclose(TrueNodeCoords[i][2],Elemliste[j][k][2],atol=1E-5):
# 				# print('Node',i,'is equal to Element',j,'Position',k)
# 				Pointer[i] = [int(j),int(k)]
# 				b=1
# 				break
# 		if b == 1:
# 			b=0
# 			# print('broke')
# 			break
# print(Pointer[0:10])
AllTemperaturesRaw= np.zeros((len(TimeIncrements),NumberElements,4))
AllTemperatures= np.zeros((len(TimeIncrements),NumberNodes))
for j in range(len(TimeIncrements)):
	o =0
	for i in range(len(Logfile)):
		try:
			if Logfile[i][0] == ' Time =' and float(Logfile[i][1]) == float(TimeIncrements[j]):
				AllTemperaturesRaw[j][o][0]=float(Logfile[i+1][1])
				AllTemperaturesRaw[j][o][1]=float(Logfile[i+1][2])
				AllTemperaturesRaw[j][o][2]=float(Logfile[i+1][3])
				AllTemperaturesRaw[j][o][3]=float(Logfile[i+1][4])
				o=o+1
				# print('jup',j,o)
				
		except:
			pass
Pointer=[]
for i in range(NumberNodes):
	Pointer.append([])
for i in range(NumberNodes):
	for u in range(NumberElements):
		for k in range(4):
			if ElemConnect[u][k] == float(i):
				Pointer[i].append([int(u),int(k)])

print(TimeIncrements)

for i in range(len(TimeIncrements)):
	for u in range(len(Pointer)):
		TempSum=0
		for k in range(len(Pointer[u])):
			TempSum=TempSum+AllTemperaturesRaw[i][int(Pointer[u][k][0])][int(Pointer[u][k][1])]
		TempAverage = TempSum/len(Pointer[u])
		AllTemperatures[i][u]= TempAverage 
pass
print('asd')

for j in range(len(TimeIncrements)):
	VTUPRINT =[]
	VTUPRINT.append(['<VTKFile', 'type="UnstructuredGrid"', 'version="0.1"', 'byte_order="LittleEndian">'])
	VTUPRINT.append(['<UnstructuredGrid>'])
	VTUPRINT.append(['<Piece', 'NumberOfPoints="'+str(NumberNodes)+'"', 'NumberOfCells="'+str(NumberElements)+'">'])
	VTUPRINT.append(['<Points>'])
	VTUPRINT.append(['<DataArray', 'type="Float64"', 'NumberOfComponents="3"', 'format="ascii">'])
	for i in range(NumberNodes):
		VTUPRINT.append(Coordinates[i])
	VTUPRINT.append(['</DataArray>'])
	VTUPRINT.append(['</Points>'])
	VTUPRINT.append(['<PointData', 'Scalars="Temperature">'])
	VTUPRINT.append(['<DataArray', 'type="Float32"', 'Name="Temperature"', 'NumberOfComponents="1"', 'format="ascii">'])
	for i in range(NumberNodes):
		VTUPRINT.append([str(AllTemperatures[j][i])])
	VTUPRINT.append(['</DataArray>'])
	VTUPRINT.append(['</PointData>'])
	VTUPRINT.append(['<Cells>'])
	VTUPRINT.append(['<DataArray', 'type="Int32"', 'Name="connectivity"', 'format="ascii">'])
	for i in range(NumberElements):
		VTUPRINT.append([str(int(ElemConnect[i][0])),str(int(ElemConnect[i][1])),str(int(ElemConnect[i][2])),str(int(ElemConnect[i][3]))])
	VTUPRINT.append(['</DataArray>'])
	VTUPRINT.append(['<DataArray', 'type="Int32"', 'Name="offsets"', 'format="ascii">'])
	for i in range(NumberElements):
		VTUPRINT.append([str(4*(i+1))])
	VTUPRINT.append(['</DataArray>'])
	VTUPRINT.append(['<DataArray', 'type="UInt8"', 'Name="types"', 'format="ascii">'])
	for i in range(NumberElements):
		VTUPRINT.append([str(10)])
	VTUPRINT.append(['</DataArray>'])
	VTUPRINT.append(['</Cells>'])
	VTUPRINT.append(['</Piece>'])
	VTUPRINT.append(['</UnstructuredGrid>'])
	VTUPRINT.append(['</VTKFile>'])
	file_object_w = open('Vtu/Heat_transfer_'+str(int(TimeIncrements[j]))+'.vtu','w')
	NewVTU = csv.writer(file_object_w, delimiter=' ',quotechar="'")
	for k in range(len(VTUPRINT)):
		NewVTU.writerow(VTUPRINT[k])
	file_object_w.close()


# pass
