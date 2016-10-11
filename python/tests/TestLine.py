"""Line Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
Line = imp.load_source('Line', './lib/Line.py')

from Vector import Vector
from Line import Line

class LineTests(unittest.TestCase):
    """Line Tests"""

    def create_line_data(self):
        return [
            [4.046, 2.836, 1.21],
            [10.115, 7.09, 3.025],
            [7.204, 3.182, 8.68],
            [8.172, 4.114, 9.883],
            [1.182, 5.562, 6.744],
            [1.773, 8.343, 9.525]
        ]

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_instance(self):
        v = Vector([2, 3])
        line = Line(v.coordinates)
        print 'line: ', line
        self.assertFalse( False )

    def test_is_parallel(self):
        self.assertFalse( 1 == 2 )

    def test_lines_equal(self):
        pass

    def test_intersection(self):
        pass

