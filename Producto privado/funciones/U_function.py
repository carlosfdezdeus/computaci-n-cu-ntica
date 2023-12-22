import numpy as np
from qiskit.quantum_info.operators import Operator

def U_gate(dim,alpha):
    # Creo la matriz con todo ceros con dimensión dim
    #dim = 2**dim
    matriz = np.zeros((dim,dim))
    
    # Asigno valores a la subdiagonal
    fila = 0
    for i in range(0,dim):
        if(alpha+i) <= dim-1:
            matriz[alpha+i,i] = 1
            fila = fila + 1
    if(fila < dim):
        for i in range (0,(dim-fila)):
            matriz[i,fila+i] = 1

    U = Operator(matriz)

    return U
    
def U_matrix(dim,alpha):
    # Creo la matriz con todo ceros con dimensión dim
    #dim = 2**dim
    matriz = np.zeros((dim,dim))
    
    # Asigno valores a la subdiagonal
    fila = 0
    for i in range(0,dim):
        if(alpha+i) <= dim-1:
            matriz[alpha+i,i] = 1
            fila = fila + 1
    if(fila < dim):
        for i in range (0,(dim-fila)):
            matriz[i,fila+i] = 1

    return matriz