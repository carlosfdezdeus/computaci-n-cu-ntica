import numpy as np
import cmath 
from qiskit.quantum_info.operators import Operator

def R_gate(dim, b, p):
    dim = 2**dim
    p = 2**p
    #Defino el valor pi y la raíz primitiva w
    pi = cmath.pi
    w = cmath.exp(2*pi*1j / p)
    # Creo la matriz con todo ceros con dimensión dim
    matriz = np.zeros((dim,dim), dtype=complex)

    for i in range(0,dim):
        matriz[i,i] = w**(b*i)

    R = Operator(matriz)
    return R

def Ri_gate(dim,b,p,i):
    dim = 2**dim
    p = 2**p
    #Defino el valor pi y la raíz primitiva w
    pi = cmath.pi
    w = cmath.exp(2*pi*1j / p)
    # Creo la matriz con todo ceros con dimensión dim
    matriz = np.zeros((dim,dim), dtype=complex)
    
    for j in range(0,dim):
        matriz[j,j] = w**(b*i)

    R = Operator(matriz)
    return R