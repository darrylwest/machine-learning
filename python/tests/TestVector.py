"""Vector Tests"""

import imp
import unittest

from decimal import Decimal, getcontext
getcontext().prec = 30

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

    def create_magnitude_data(self):
        return [
            [-0.221, 7.437],
            [8.813, -1.331, -6.247]
        ]

    def create_direction_data(self):
        return [
            [5.581, -2.136],
            [1.996, 3.108, -4.554]
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
            [-4.496, -8.755, 7.103],
            [1, 3, -2],
            [-2, 4, -1]
        ]

    def create_angle_data(self):
        return [
            [3.183, -7.627],
            [-2.668, 5.319],
            [7.35, 0.221, 5.188],
            [2.751, 8.259, 3.985],
            [1, 3, -2],
            [-2, 4, -1]
        ]
    
    def create_projection_data(self):
        return [
            [3.039, 1.879],
            [0.825, 2.036],
            [-9.88, -3.264, -8.159],
            [-2.155, -9.353, -9.473],
            [3.009, -6.172, 3.692, -2.51],
            [6.404,-9.144, 2.759, 8.718]
        ]

    def create_cross_product_data(self):
        return [
            [1, -7, 1],
            [5, 2, 4],
            [5, 3, -2],
            [-1, 0, 3],
            [8.462, 7.893, -8.187],
            [6.984, -5.975, 4.778],
            [-8.987,-9.838, 5.031],
            [-4.268,-1.861,-8.866],
            [1.5, 9.547, 3.691],
            [-6.007, 0.124, 5.772]
        ]

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_instance(self):
        data = [1, 2, 3]
        v = Vector(data)
        self.assertEqual(v.dimension, len(data))
        w = Vector(v.coordinates)
        self.assertEqual(v, w)

    def test_plus_minus(self):
        data = self.create_plus_minus_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))        
        self.assertEqual(str(v1.plus(v2)), str(Vector([7.089, -7.23])))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))        
        self.assertEqual(str(v1.minus(v2)), str(Vector([15.342, 7.337])))

    def test_times(self):
        data = self.create_scalar_data()

        scalar = data.pop(0)
        v1 = Vector(data.pop(0))
        self.assertEqual(str(v1.times(scalar)), str(Vector([12.3821, -7.4989, -2.3564])))

    def test_divide(self):
        v = Vector([2, 4, 6, 8])
        v = v.divide(2)

        expects = (Decimal(1), Decimal(2), Decimal(3), Decimal(4))
        self.assertEqual(v.coordinates, expects)

    def test_pow(self):
        v = Vector([3, 2])
        v = v.pow(3)
        expects = (Decimal(27), Decimal(2*2*2))
        self.assertEqual(v.coordinates, expects)

    def test_sqr(self):
        v = Vector([2, 4])
        v = v.sqr()
        expects = (Decimal(4), Decimal(16))
        self.assertEqual(v.coordinates, expects)

    def test_magnitude(self):
        data = self.create_magnitude_data()

        v1 = Vector(data.pop(0))
        self.assertEqual(round(v1.magnitude(), 9), 7.440282925)

        v1 = Vector(data.pop(0))
        self.assertEqual(round(v1.magnitude(), 9), 10.884187567)

    def test_normalize(self):
        pass
    
    def test_direction(self):
        data = self.create_direction_data()

        v1 = Vector(data.pop(0))
        self.assertEqual(str(v1.direction()), str(Vector([0.9339, -0.3574])))

        v1 = Vector(data.pop(0))
        self.assertEqual(str(v1.direction()), str(Vector([0.3404, 0.53, -0.7766])))

    def test_dot(self):
        data = self.create_dot_product_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.dot(v2), 3), -41.382)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.dot(v2), 3), 56.397)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.dot(v2), 3), 12.0)

    def test_angle_with(self):
        data = self.create_angle_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.angle_with(v2), 3), 3.072)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.angle_with(v2, True), 3), 60.276)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        self.assertEqual(round(v1.angle_with(v2, True), 3), 45.585)

    def test_orthogonal(self):
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

    def test_projection(self):
        data = self.create_projection_data()

        vector = Vector(data.pop(0))
        basis = Vector(data.pop(0))
        para = vector.component_parallel_to(basis)
        self.assertEqual(str(para), str(Vector([1.0826, 2.6717])))

        vector = Vector(data.pop(0))
        basis = Vector(data.pop(0))
        perp = vector.component_orthogonal_to(basis)
        self.assertEqual(str(perp), str(Vector([-8.3501, 3.3761, -1.4337])))

        vector = Vector(data.pop(0))
        basis = Vector(data.pop(0))
        para = vector.component_parallel_to(basis)
        perp = vector.component_orthogonal_to(basis)
        self.assertTrue(str(para), str(Vector([1.9685, -2.8108, 0.8481, 2.6798])))
        self.assertTrue(str(perp), str(Vector([1.0405, -3.3612, 2.8439, -5.1898])))

    def test_cross_product(self):
        data = self.create_cross_product_data()

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        xp = v1.cross_product_of(v2)
        self.assertEqual(str(xp), str(Vector([-30, 1, 37])))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        xp = v1.cross_product_of(v2)
        self.assertEqual(str(xp), str(Vector([9.0, -13.0, 3.0])))
        area = xp.area()
        self.assertEqual(round(area, 5), 16.09348)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        xp = v1.cross_product_of(v2)
        self.assertEqual(str(xp), str(Vector([-11.2046, -97.6094, -105.6852])))

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        xp = v1.cross_product_of(v2)
        area = xp.area()

        self.assertEqual(round(area, 5), 142.12222)

        v1 = Vector(data.pop(0))
        v2 = Vector(data.pop(0))
        xp = v1.cross_product_of(v2)
        area = xp.area() / 2.0
        self.assertEqual(round(area, 5), 42.56494)


