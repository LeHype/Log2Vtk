1. Build your Fortran Subroutine. 
   - Store the values you want to visulize in an Array 
   - If there are multiple comonents in a Variable, for example deformation store them as follows:
   - ExampleArrayDeformation = [x1,y1,z1, x2,y2,z2 ...ect] where x,y and z are the components and 1,2, ect are the nodes where the variable occurs
   - You can specify an arbitrary number of components, so if you want to for example include the van mises stress in addition to the individual components you can shape the array to be :
   - Stress = [ sx1,sy1,sz1,yxy1,yyz1,yzx1,mises1,sx1.. ect]
   - Right now the components will have no label and will be displayed as [1,2,3,4 ect.]
 2.  Run the suplied preprocessing Fortran Subroutine

   ```fortran
 call ParaviewPreProcessing('U',3,U,TIME,JELEM,NNODE)
``` 
  Where in order of appearance:
    'U' --> Unique IDentifer: Unique Name that will be the Name of the Variable in the Paraview Visulization. One character Ideifiers are not mandatory but longer names could lead to bugs. Identifier U is mandatory for the Deformation! 
    '3' --> The number of components the Variable has. see 1. 
    'Time' --> The Current step Time 
    'JELEM' --> The current Element 
    'NNODE' --> Number of Nodes per Element 
   This syntax is mandatory.! 
   \\Todo: make an option to label individual components and make it possible to name Deformation something else.

  The desired Variables will be written to the Log File. 

3. The next Step is to open the config.txt file in the Log2Vtk folder. There you need to specify the unique identifiers from above as well as the File Paths and the element type. 

3.5 There is a rudimentary GUI for the configurations but does not work fully yet

4. Run the main skript and open the resulting vtu files with Paraview. --> Done. 

There is a Samples Folder That contain a Dummy input file, and a Dummy Fortran File that can be used to try out the functionalities also please watch the video tutorial before using the Script. If any problems or errors occur feel free to ask me. 

\\TODO Finish GUI 