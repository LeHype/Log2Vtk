import numpy as np 
A = [[1,1,1],[2,2,2],[3,3,3]]
A = [(x-1,x) for y in A for x in y]

print(A)
