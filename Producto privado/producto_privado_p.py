from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram
from funciones.encondings import encondings
from funciones.U_function import U_matrix
from funciones.R_function import R_matrix
import numpy as np
import random

p = 5
alpha = 2   
a = 2
b = 4
n = 3
beta = 2

# Elijo uno de los encodigs al azar
enconding = random.randint(1, 4)
print(enconding)
Xa_A, Xb_B, Za_A, Zb_B = encondings(1, a, b, alpha, beta, n, p)

# print(Xa_A)
# print(Xb_B)
# print(Za_A)
# print(Zb_B)

# Creo las puertas R y U
X_Xa_A = U_matrix(n, Xa_A)
X_Xb_B = U_matrix(n, Xb_B)
Z_Za_A = R_matrix(n, Za_A, p)
Z_Zb_B = R_matrix(n, Zb_B, p)

#print(X_Xa_A)
# print(X_Xb_B)
# print(Z_Za_A)
#print(Z_Zb_B)
#print(np.dot(X_Xa_A,Z_Za_A))
# Crear la matriz identidad 5x5
I3 = np.identity(3)

# Transponer las filas
I3_t = I3.T

# Convertir la matriz a una matriz 25x1
vec_1p = I3_t.reshape(-1, 1)

vec_1p_t = vec_1p.T

# print(vec_1p)
# print(vec_1p_t)

fi_00 = vec_1p*vec_1p_t

#print(fi_00)

producto_tensor = np.kron(np.dot(X_Xa_A,Z_Za_A), np.dot(X_Xb_B,Z_Zb_B))

#print(producto_tensor)

fi_ab = np.dot(producto_tensor,fi_00)
#producto_tensor*fi_00
#print(fi_ab)

# Simula el circuito para obtener los resultados
simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(transpile(qc, simulator)).result()

# Convierte el estado final en una matriz de densidad
density_result = np.outer(result.get_statevector(), np.conj(result.get_statevector()))

# Visualiza la matriz de densidad convertida en resultados
counts = {'0': density_result[0, 0], '1': density_result[1, 1]}
plot_histogram(counts)