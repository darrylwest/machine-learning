"""Line Tests"""

import imp
import unittest

Vector = imp.load_source('Vector', './lib/Vector.py')
Line = imp.load_source('Line', './lib/Line.py')

from Vector import Vector
from Line import Line

class LineTests(unittest.TestCase):
    """Line Tests"""

    def test_instance(self):
        v = Vector([1, 3, 6])
        self.assertFalse( False )

if __name__ == '__main__':
    unittest.main()
