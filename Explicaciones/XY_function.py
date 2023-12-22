# Importo todo de qiskit
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram

def XY_gate():
    qr = QuantumRegister(1)
    qc = QuantumCircuit(qr, name='XY')
    qc.x(qr[0])
    qc.y(qr[0])
    return qc