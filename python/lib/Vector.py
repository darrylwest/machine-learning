
"""Vector utilities"""

from decimal import Decimal, getcontext
from math import acos, degrees, sqrt, pi

getcontext().prec = 30

class Vector(object):
    """Vector class methods for simple vector operations"""

    __version__ = '0.90.10'
    __author__ = 'darryl.west@raincitysoftware.com'

    CANNOT_NORMALIZE_ZERO_VECTOR = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT = 'No unique parallel component'

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
        return Vector([Decimal(scalar) * x for x in self.coordinates])

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

    def normalized(self):
        """nomalize the vector"""
        try:
            magnitude = self.magnitude()
            return self.times(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise self.CANNOT_NORMALIZE_ZERO_VECTOR

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
            uv1 = self.normalized()
            uv2 = vector.normalized()

            # acos throws if not roundedq
            dot = round(uv1.dot_product(uv2), 14)

            angle = acos(dot)

            if in_degrees:
                return degrees(angle)
            else:
                return angle

        except ValueError as exe:
            if str(exe) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception('Cannot compute an angle with a zero vector')
            else:
                raise exe

    def is_parallel_to(self, vector):
        """return true if the two vectors are parallel"""

        if self.is_zero() or vector.is_zero():
            return True

        angle = self.angle_with(vector)

        return angle == 0 or angle == pi

    def is_orthogonal_to(self, vector, tolerance=1e-10):
        """return true if the vectors are perpendicular"""
        return abs(self.dot_product(vector)) < tolerance

    def is_zero(self, tolerance=1e-10):
        """return true if my vertor is very close to zero"""
        return self.magnitude() < tolerance

    def component_orthogonal_to(self, basis):
        """calculate the component orthogonal to basis"""
        try:
            proj = self.component_parallel_to(basis)
            return self.minus(proj)

        except ValueError as exe:
            if str(exe) == self.NO_UNIQUE_PARALLEL_COMPONENT:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT)
            else:
                raise exe

    def component_parallel_to(self, basis):
        """calculate the component parallel to the basis"""
        try:
            uvec = basis.normalized()
            weight = self.dot_product(uvec)
            return uvec.times(weight)

        except ValueError as exe:
            if str(exe) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR)
            else:
                raise exe

    def cross_product_of(self, vector):
        """calculate the cross product and return the vector"""
        print self, vector
        return Vector([0, 0, 0])

    def parallelogram_area_of(self, vector):
        """calculate the area of the parallelogram from vector"""
        print self, vector
        return 0.0

    def __str__(self):
        numbers = [round(x, 4) for x in self.coordinates]
        return 'Vector: {}'.format(numbers)

    def __eq__(self, vector):
        return self.coordinates == vector.coordinates
