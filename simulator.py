from typing import Type
import numpy as np

C = None
baseGates = {
    'i': np.array([[1, 0], [0, 1]]),
    'x': np.array([[0, 1], [1, 0]]),
    'y': np.array([[0, -1j], [1j, 0]]),
    'z': np.array([[1, 0], [0, -1]]),
    'h': (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]),
    's': np.array([[1, 0], [0, 1j]]),
    't': np.array([[1, 0], [0, np.exp(1j * np.pi/4)]])
}

class Circuit:

    def __init__(self, qubitCount=2):
        if type(qubitCount) is not int:
            raise TypeError('Qubit count must be an int.')
        if qubitCount <= 0:
            raise ValueError('Qubit count must be positive.')
        
        self.qubitCount = qubitCount
        self.stateVec = np.zeros(2**self.qubitCount)
        self.stateVec[0] = 1

    def __str__(self):
        return str(self.stateVec)

    def applySingleQubitGates(self, operators):
        if type(operators) is not list:
            raise TypeError('Operators must be given in a list.')
        if len(operators) > self.qubitCount:
            raise ValueError('Operator count exceeds qubit count.')
        for gate in operators:
            if gate not in baseGates:
                raise ValueError('All operators must be accepted base gates.')
                # TODO: Change this to allow for any unitary matrices.

        while len(operators) < self.qubitCount:
            operators.append('i')
        
        if self.qubitCount == 1:
            self.stateVec = self.stateVec @ baseGates[operators[0]]

        i = len(operators)
        op = np.kron(baseGates[operators[i-2]], baseGates[operators[i-1]])
        for j in range(i-3, -1, -1):
            op = np.kron(baseGates[operators[j]], op)

        self.stateVec = self.stateVec @ op

    def applyControlledXGate(self, operator):
        pass