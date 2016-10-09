"""Vector Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
from Vector import Vector

class VectorTests(unittest.TestCase):
    """Vector Tests"""

    # simulate the fixture data
    def create_plus_minus_data(self):
        return [
            [8.218, -9.341],
            [-1.129, 2.111],
            [7.119, 8.215],
            [-8.223, 0.878]
        ]
    
    def create_scalar_data(self):
        return [
            7.41,
            [1.671, -1.012, -0.318]
        ]

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

    def create_dot_product_data(self):
        return [
            [7.887, 4.138],
            [-8.802, 6.776],
            [-5.955, -4.904, -1.874],
            [-4.496, -8.755, 7.103]
        ]

    def create_angle_data(self):
        return [
            [3.183, -7.627],
            [-2.668, 5.319],
            [7.35, 0.221, 5.188],
            [2.751, 8.259, 3.985]
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

    def test_plus_minus(self):
        """test vector addition"""
        data = self.create_plus_minus_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))        
        self.assertEqual(str(v1.plus(v2)), str(Vector([7.089, -7.23])))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))        
        self.assertEqual(str(v1.minus(v2)), str(Vector([15.342, 7.337])))

    def test_times(self):
        """test vector scalar multiplication"""
        data = self.create_scalar_data()

        scalar = data.pop(0)
        v1 = Vector(data.pop(0))
        self.assertEqual(str(v1.times(scalar)), str(Vector([12.3821, -7.4989, -2.3564])))

    def test_divide(self):
        """test vector scalar division"""
        pass

    def test_pow(self):
        """test vector raised to the power of n"""
        pass

    def test_sqr(self):
        """test vector squared"""
        pass

    def test_sum(self):
        """test vector summation"""
        pass

    def test_magnitude(self):
        """test vector's magnitude"""
        pass

    def test_normalize(self):
        """test the normalization of a vector"""
        pass
    
    def test_direction(self):
        """test the vector direction"""
        pass

    def test_dot_product(self):
        """tset the dot product"""
        data = self.create_dot_product_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.dot_product(v2), 3), -41.382)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.dot_product(v2), 3), 56.397)

    def test_angle_with(self):
        """test the angle with"""
        data = self.create_angle_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.angle_with(v2), 3), 3.072)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.angle_with(v2, True), 3), 60.276)

    def test_orthogonal(self):
        """insure that the datasets are orthogonal or not"""
        data = self.create_parallel_orthogonal_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_orthogonal_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_orthogonal_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertTrue(v1.is_orthogonal_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertTrue(v1.is_orthogonal_to(v2))
        
    def test_is_parallel(self):
        """insure that the datasets are parallel or not"""
        
        data = self.create_parallel_orthogonal_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        # print 'debug: ', v1, v2
        self.assertTrue(v1.is_parallel_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_parallel_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertFalse(v1.is_parallel_to(v2))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertTrue(v1.is_parallel_to(v2))

if __name__ == '__main__':
    unittest.main()
