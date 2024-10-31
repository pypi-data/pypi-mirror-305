import unittest
from gate_manager import Gate, GatesGroup  

class TestGate(unittest.TestCase):
    def test_initialization(self):
        gate = Gate(name="TestGate", label="P1", read_index=0)
        self.assertEqual(gate.name, "TestGate")
        self.assertEqual(gate.label, "T1")
        self.assertEqual(gate.read_index, 0)

class TestGatesGroup(unittest.TestCase):
    def test_initialization(self):
        gates_group = GatesGroup()
        self.assertEqual(GatesGroup.gates, [])


if __name__ == '__main__':
    unittest.main()
