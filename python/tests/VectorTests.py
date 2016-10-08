"""Vector Tests"""

import unittest
import imp

Vector = imp.load_source('Vector', './lib/Vector.py')

from Vector import Vector

class VectorTests(unittest.TestCase):
    """Vector Tests"""

    # def setUp(self):
    # def tearDown(self):

    def test_instance(self):
        """test the vector instance"""
        list = [1, 2, 3]
        v = Vector(list)
        self.assertEqual(v.dimension, len(list))

if __name__ == '__main__':
    unittest.main()
