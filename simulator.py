import numpy as np

i = np.array([[1, 0], [0, 1]])
x = np.array([[0, 1], [1, 0]])
y = np.array([[0, -1j], [1j, 0]])
z = np.array([[1, 0], [0, -1]])
h = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
s = np.array([[1, 0], [0, 1j]])
t = np.array([[1, 0], [0, np.exp(1j * np.pi/4)]])

class Circuit:

    def __init__(self, qubitCount=2):
        self.qubitCount = qubitCount
        self.stateVec = np.zeros(2**self.qubitCount)
        self.stateVec[0] = 1

    def __str__(self):
        return str(self.stateVec)


circ = Circuit(3)
print(circ)