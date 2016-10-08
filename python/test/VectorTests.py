"""Vector Tests"""

import unittest
import imp

Vector = imp.load_source('Vector', './src/Vector.py')

from Vector import Vector

class VectorTests(unittest.TestCase):
    """Vector Tests"""

    def test_instance(self):
        """test the vector instance"""
        v = Vector([1, 2, 3])
        print v, self

if __name__ == '__main__':
    unittest.main()
