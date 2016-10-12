"""Plane Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
Line = imp.load_source('Line', './lib/Line.py')

from Vector import Vector
from Line import Line, MyDecimal

from decimal import Decimal

class PlaneTests(unittest.TestCase):
    """plane tests"""

    def create_plane_data(self):
        return [
            [-0.412, 3.806, 0.728, -3.46],
            [1.03, -9.515, -1.82, 8.65],
            [2.611, 5.528, 0.283, 4.6],
            [7.715, 8.306, 5.342, 3.76],
            [-7.926, 8.625, -7.217, -7.952],
            [-2.642, 2.875, -2.404, -2.443]
        ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertTrue( True )

    def test_equal(self):
        self.assertTrue( True )

    def test_is_parallel(self):
        self.assertTrue( True )