
"""Vector utilities"""

class Vector(object):
    """Vector class methods for simple vector operations"""

    __version__ = '0.90.10'
    __author__ = 'darryl.west@raincitysoftware.com'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        return Vector([x / scalar for x in self.coordinates])

    def pow(self, num):
        """scalar power"""
        return Vector([pow(x, num) for x in self.coordinates])

    def sqr(self):
        """square the elements"""
        return self.pow(2)

    def sum(self):
        """sum the elements"""
        return sum(self.coordinates)

    def magnitude(self):
        """return the vector's magnitude"""
        return pow(sum([x**2 for x in self.coordinates]), 0.5)

    def direction(self):
        """return the vector direction"""
        try:
            mag = self.magnitude()
            return self.divide(mag)

        except ZeroDivisionError:
            raise Exception('cannot normalize the zero vector')

    def dot_product(self, vector):
        """return the dot product"""
        print vector
        return Vector(self.coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, vector):
        return self.coordinates == vector.coordinates

if __name__ == '__main__':
    V = Vector([7.887, 4.138])
    W = Vector([-8.802, 6.776])
    print V, W, '.p: ', V.dot_product(W)
