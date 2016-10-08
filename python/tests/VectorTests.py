"""Vector Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
from Vector import Vector

class VectorTests(unittest.TestCase):
    """Vector Tests"""

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_instance(self):
        """test the vector instance"""
        data = [1, 2, 3]
        v = Vector(data)
        self.assertEqual(v.dimension, len(data))
        w = Vector(v.coordinates)
        self.assertEqual(v, w)

    def test_parallel(self):
        """insure that the datasets are parallel"""
        
        # simulate reading these from a fixture file...
        
        data = [
            [-7.579, -7.88],
            [22.737, 23.64]
        ]

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))

        # print v1, v2
        self.assertTrue(v1.parallel(v1))


if __name__ == '__main__':
    unittest.main()
