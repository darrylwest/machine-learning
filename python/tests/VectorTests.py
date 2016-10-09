"""Vector Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
from Vector import Vector

class VectorTests(unittest.TestCase):
    """Vector Tests"""

    # simulate the fixture data
    def create_parallel_orthogonal_data(self):
        return [
            [-7.579, -7.88],
            [22.737, 23.64],
            [-2.029, 9.97, 4.172],
            [-9.231, -6.639,-7.245],
            [-2.328, -7.284, -1.214],
            [-1.821, 1.072, -2.94],
            [2.118, 4.827],
            [0, 0]
        ]

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

    def test_orthogonal(self):
        """insure that the datasets are orthogonal"""
        data = self.create_parallel_orthogonal_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_orthogonal_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_orthogonal_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        # print 'angle: ', v1.dot_product(v2)
        self.assertTrue(v1.is_orthogonal_to(v2))
        

    def test_parallel(self):
        """insure that the datasets are parallel"""
        
        data = self.create_parallel_orthogonal_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))

        # print v1, v2
        # self.assertTrue(v1.parallel_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))

        # print v1, v2
        # self.assertTrue(v1.parallel_to(v2))


if __name__ == '__main__':
    unittest.main()
