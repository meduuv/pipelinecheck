import unittest
from pipelinecheck import validate

class PipelineCheckTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate([{"name":"build","command":"make"}]), [])
    def test_invalid(self): self.assertEqual(validate([{}]), ["step[0]: missing name", "step[0]: missing command"])

if __name__ == "__main__": unittest.main()
