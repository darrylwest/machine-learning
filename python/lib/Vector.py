
"""Vector utilities"""

from decimal import Decimal, getcontext
from math import acos, degrees, sqrt, pi

getcontext().prec = 30

class Vector(object):
    """Vector class methods for simple vector operations"""

    __version__ = '0.90.10'
    __author__ = 'darryl.west@raincitysoftware.com'

    ZERO = Decimal(0)

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be non-empty')

        except TypeError:
            raise TypeError('The coordinates mus be an iterable')

    def plus(self, vector):
        """add the two vectors"""
        return Vector([x + y for x, y in zip(self.coordinates, vector.coordinates)])

    def minus(self, vector):
        """subtract the two vectors"""
        return Vector([x - y for x, y in zip(self.coordinates, vector.coordinates)])

    def times(self, scalar):
        """scalar multiply"""
        return Vector([scalar * x for x in self.coordinates])

    def divide(self, scalar):
        """scalar divide"""
        return Vector([Decimal(x) / scalar for x in self.coordinates])

    def pow(self, num):
        """scalar power"""
        return Vector([pow(x, Decimal(num)) for x in self.coordinates])

    def sqr(self):
        """square the elements"""
        return self.pow(2)

    def sum(self):
        """sum the elements"""
        return sum(self.coordinates)

    def magnitude(self):
        """return the vector's magnitude"""
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))

    def direction(self):
        """return the vector direction"""
        try:
            mag = self.magnitude()
            return self.divide(mag)

        except ZeroDivisionError:
            raise Exception('cannot normalize the zero vector')

    def dot_product(self, vector):
        """return the dot product"""
        return sum([x * y for x, y in zip(self.coordinates, vector.coordinates)])

    def angle_with(self, vector, in_degrees=False):
        """return the angle between two vectors in radians"""

        try:
            dot = self.dot_product(vector)
            angle_r = acos(dot / (self.magnitude() * vector.magnitude()))

            if in_degrees:
                return degrees(angle_r)
            else:
                return angle_r

        except Exception as ex:
            raise ex

    def parallel_to(self, vector):
        """return true if the two vectors are parallel"""

        if self.is_zero() or vector.is_zero:
            return True

        angle = self.angle_with(vector)
        print 'angle: ', angle

        return angle == 0 or angle == pi

    def is_orthogonal_to(self, vector, tolerance=1e-10):
        """return true if the vectors are perpendicular"""
        return abs(self.dot_product(vector)) < tolerance

    def is_zero(self, tolerance=1e-10):
        """return true if my vertor is very close to zero"""
        return self.magnitude() < tolerance

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, vector):
        return self.coordinates == vector.coordinates

if __name__ == '__main__':
    V = Vector([3.183, -7.627])
    W = Vector([-2.668, 5.319])
    print V, W, 'dot: ', V.dot_product(W), ', angle: ', V.angle_with(W)

    V = Vector([7.35, 0.221, 5.188])
    W = Vector([2.751, 8.259, 3.985])

    print V, W, 'dot: ', V.dot_product(W), ', angle: ', V.angle_with(W, True)
