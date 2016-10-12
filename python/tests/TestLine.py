"""Line Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
Line = imp.load_source('Line', './lib/Line.py')

from Vector import Vector
from Line import Line, MyDecimal

from decimal import Decimal

class LineTests(unittest.TestCase):
    """Line Tests"""

    def create_line_data(self):
        """data defined as Ax + By = k"""
        return [
            [4.046, 2.836, 1.21],
            [10.115, 7.09, 3.025], # same line
            [7.204, 3.182, 8.68],
            [8.172, 4.114, 9.883], # intersection
            [1.182, 5.562, 6.744],
            [1.773, 8.343, 9.525] # parallel
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
        data = self.create_line_data()

        ax1, by1, k1 = data.pop(0)
        ax2, by2, k2 = data.pop(0)

        v1 = Vector([ax1, by1])
        v2 = Vector([ax2, by2])

        line1 = Line(v1.coordinates, k1)
        line2 = Line(v2.coordinates, k2)

        # print 'line1 ', line1, line1.normal_vector
        # print 'line2 ', line2, line2.normal_vector

        self.assertTrue( v1.is_parallel_to( v2 ) )
        self.assertTrue(line1.is_parallel_to(line2))

        # now, is it the same line?
        ax1, by1, k1 = data.pop(0)
        ax2, by2, k2 = data.pop(0)

        v1 = Vector([ax1, by1])
        v2 = Vector([ax2, by2])

        line1 = Line(v1.coordinates, k1)
        line2 = Line(v2.coordinates, k2)

        # print 'line1 ', line1, line1.normal_vector
        # print 'line2 ', line2, line2.normal_vector
        self.assertFalse(line1.is_parallel_to(line2))

        ax1, by1, k1 = data.pop(0)
        ax2, by2, k2 = data.pop(0)

        line1 = Line([ax1, by1], k1)
        line2 = Line([ax2, by2], k2)

        # print 'line1 ', line1, line1.normal_vector
        # print 'line2 ', line2, line2.normal_vector
        self.assertTrue(line1.is_parallel_to(line2))


    def test_calc_y_intercept(self):
        data = self.create_line_data()

        ax1, by1, k1 = data.pop(0)
        line = Line([ax1, by1], k1)


    def test_lines_equal(self):
        pass

    def test_intersection(self):
        data = self.create_line_data()

        ax1, by1, k1 = data.pop(0)
        ax2, by2, k2 = data.pop(0)

        line1 = Line([ax1, by1], k1)
        line2 = Line([ax2, by2], k2)

        result = line1.calc_intersection(line2)

        print 'result: ', result
        self.assertEqual(result, (True, True, None, None))

        ax1, by1, k1 = data.pop(0)
        ax2, by2, k2 = data.pop(0)

        line1 = Line([ax1, by1], k1)
        line2 = Line([ax2, by2], k2)

        result = line1.calc_intersection(line2)

        print 'result: ', result
        p, s, x, y = result
        self.assertFalse( p )
        self.assertFalse( s )
        self.assertEqual(round(x, 3), 1.173)
        self.assertEqual(round(y, 3), 0.073)

    def test_mydecimal(self):
        d = MyDecimal(Decimal(0.4))
        self.assertFalse(d.is_near_zero())
        d = MyDecimal(Decimal(-0.000004))
        self.assertFalse(d.is_near_zero())
        d = MyDecimal(Decimal(0.000))
        self.assertTrue(d.is_near_zero())

