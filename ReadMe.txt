1. Build your Fortran Subroutine. 
   - Store the values you want to visulize in an Array 
   - If there are multiple comonents in a Variable, for example deformation store them as follows:
   - ExampleArrayDeformation = [x1,y1,z1, x2,y2,z2 ...ect] where x,y and z are the components and 1,2, ect are the nodes where the variable occurs
   - You can specify an arbitrary number of components, so if you want to for example include the van mises stress in addition to the individual components you can shape the array to be :
   - Stress = [ sx1,sy1,sz1,yxy1,yyz1,yzx1,mises1,sx1.. ect]
   - Right now the components will have no label and will be displayed as [1,2,3,4 ect.]
 2.  Run the suplied preprocessing Fortran Subroutine 
   - 
   This syntax is mandatory.! 
   \\Todo: make an option to label individual components 