import csv
import numpy as np

from tkinter import *
from resources.Gui import *
from resources.ConfigFile import *
from resources.InpFile2Array import *
from resources.VariableClass import *
from resources.Log2Array import *
from resources.WriteVtk import *
from resources.ElementType import *
def main():

	path,filename,vtupath,UniqueId,Components,Deformation,ElementGeom = ReadConfig('config.txt')

	UniqueGeometryId = identifyElementType(ElementGeom)

	NumberNodes,NodalCoordinates,NumberElements,ElementConnectivities = NodesAndElementsFromInput(path, filename)

	UniqueVariables = LogFileReader(path, filename, ElementConnectivities,NumberNodes,UniqueId,Components)

	WriteVtk(vtupath, filename, UniqueVariables,UniqueId, NumberElements, ElementConnectivities, NumberNodes, NodalCoordinates,Deformation,UniqueGeometryId)

	pass
if __name__=='__main__' :
	main()
	sys.exit(2)
pass
