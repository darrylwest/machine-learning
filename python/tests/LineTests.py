"""Line Tests"""

import imp
import unittest

Line = imp.load_source('Line', './lib/Line.py')

class LineTests(unittest.TestCase):
    """Line Tests"""

if __name__ == '__main__':
    unittest.main()
