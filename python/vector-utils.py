
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

    def times_scalar(self, c):
        coor = [ c*x * x in self.coordinates ]
        return Vector( coor )

    def pow(self, n):
        return Vector( map(lambda x: pow(x, n), self.coordinates) )

    def sqr(self):
        return self.pow( 2 )

    def sum(self):
        # return reduce((lambda x, y: x + y), self.coordinates )
        return sum(self.coordinates)

    def magnitude(self):
        return pow( reduce((lambda x, y: x ** 2 + y ** 2), self.coordinates ), 0.5 )

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

if __name__ == '__main__':
    v = Vector([ -1.221, 7.437 ])
    print v

    # print v.sqr()
    # print v.sum()
    print v.magnitude()

