
# @class Vector
# dpw 2016-10-08

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be non-empty');

        except TypeError:
            raise TypeError('The coordinates mus be an iterable')

    def plus(self, v):
        coor = [ x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector( coor )

    def minus(self, v):
        coor = [ x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector( coor )

    def times(self, scalar):
        return Vector([ scalar * x for x in self.coordinates ])

    def divide(self, scalar):
        return Vector( [ x / scalar for x in self.coordinates ])

    def pow(self, n):
        return Vector( [ pow(x, n) for x in self.coordinates ] )

    def sqr(self):
        return self.pow( 2 )

    def sum(self):
        return sum(self.coordinates)

    def magnitude(self):
        # return pow( sum( map(lambda x: pow(x, 2), self.coordinates) ), 0.5)
        return pow( sum([ x**2 for x in self.coordinates ]), 0.5 )

    def direction(self):
        try:
            mag = self.magnitude()
            return self.divide( mag )

        except ZeroDivisionError:
            raise Exception('cannot normalize the zero vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

if __name__ == '__main__':
    v = Vector([ -0.221, 7.437 ])
    print v, 'mag-> ', v.magnitude()
    print v, 'pow-> ', v.pow(2)

    v = Vector([ 8.813, -1.331, -6.247 ])
    print v, 'mag-> ', v.magnitude()

    v = Vector([ 5.581, -2.136 ])
    print v, 'dir->', v.direction()

    v = Vector([1.996, 3.108, -4.554])
    print v, 'dir->', v.direction()
