"""Plane Tests"""

import imp
import unittest

Plane = imp.load_source('Plane', './lib/Plane.py')
from Plane import Plane

class PlaneTests(unittest.TestCase):
    """plane tests"""

    def create_plane_data(self):
        return [
            [-0.412, 3.806, 0.728, -3.46],
            [1.03, -9.515, -1.82, 8.65], # equal
            [2.611, 5.528, 0.283, 4.6],
            [7.715, 8.306, 5.342, 3.76], # parallel
            [-7.926, 8.625, -7.217, -7.952],
            [-2.642, 2.875, -2.404, -2.443] # not parallel
        ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertTrue( True )

    def test_equal(self):
        data = self.create_plane_data()

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)
        self.assertTrue(plane1 == plane2)

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)

        self.assertFalse(plane1.is_parallel_to(plane2))
        self.assertFalse(plane1 == plane2)

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)

        self.assertFalse(plane1 == plane2)

    def test_is_parallel(self):
        data = self.create_plane_data()

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)

        print plane1
        print plane2

        self.assertTrue(plane1.is_parallel_to(plane2))
        self.assertTrue(plane1 == plane2)

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)

        self.assertFalse(plane1.is_parallel_to(plane2))

        ax1, by1, cz1, k1 = data.pop(0)
        ax2, by2, cz2, k2 = data.pop(0)

        plane1 = Plane([ax1, by1, cz1], k1)
        plane2 = Plane([ax2, by2, cz2], k2)

        self.assertFalse(plane1.is_parallel_to(plane2))