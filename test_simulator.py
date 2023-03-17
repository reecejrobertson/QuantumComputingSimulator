from re import X
import pytest
import simulator as sim

def test_createCircuit():
    circ = sim.Circuit(1)
    assert str(circ) == '[1. 0.]', 'failed on circuit with one qubit'

    circ = sim.Circuit(2)
    assert str(circ) == '[1. 0. 0. 0.]', 'failed on circuit with two qubits'

    with pytest.raises(TypeError) as err:
        sim.Circuit('Hello')
    assert err.value.args[0] == 'Qubit count must be an int.'

    with pytest.raises(ValueError) as err:
        sim.Circuit(0)
    assert err.value.args[0] == 'Qubit count must be positive.'

def test_applySingeQubitGates():
    circ = sim.Circuit(3)
    with pytest.raises(TypeError) as err:
        circ.applySingleQubitGates('h')
    assert err.value.args[0] == 'Operators must be given in a list.'

    circ = sim.Circuit(3)
    with pytest.raises(ValueError) as err:
        circ.applySingleQubitGates(['h', 'h', 'h', 'h'])
    assert err.value.args[0] == 'Operator count exceeds qubit count.'

    circ = sim.Circuit(3)
    with pytest.raises(ValueError) as err:
        circ.applySingleQubitGates(['Hello'])
    assert err.value.args[0] == 'All operators must be accepted base gates.'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates([])
    assert str(circ) == '[1. 0. 0. 0. 0. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['x'])
    assert str(circ) == '[0. 0. 0. 0. 1. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['x', 'i'])
    assert str(circ) == '[0. 0. 0. 0. 1. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['x', 'i', 'i'])
    assert str(circ) == '[0. 0. 0. 0. 1. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['i', 'x'])
    assert str(circ) == '[0. 0. 1. 0. 0. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['i', 'x', 'i'])
    assert str(circ) == '[0. 0. 1. 0. 0. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['i', 'i', 'x'])
    assert str(circ) == '[0. 1. 0. 0. 0. 0. 0. 0.]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['h', 'h'])
    assert str(circ) == '[0.5 0.  0.5 0.  0.5 0.  0.5 0. ]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['h', 'i', 'h'])
    assert str(circ) == '[0.5 0.5 0.  0.  0.5 0.5 0.  0. ]'

    circ = sim.Circuit(3)
    circ.applySingleQubitGates(['x'])
    circ.applySingleQubitGates(['h', 'h'])
    assert str(circ) == '[ 0.5  0.   0.5  0.  -0.5  0.  -0.5  0. ]'
