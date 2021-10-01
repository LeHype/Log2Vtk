import numpy as np 
def identifyElementType(name):
    name=name.lower()
    Lookup={
'tet':10,
'hex':12,
'triangle':5,
'quadratic':9,
'tet_quad' :24,  
'hex_quad' :25, 
'tri_quad':22,
'quad_quad':28

    }
    return(Lookup.get(name))
