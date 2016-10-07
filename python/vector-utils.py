
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

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

if __name__ == '__main__':
    v = Vector([1, 2, 3])
    print v

    v = v.plus(Vector([ 4, 5, 6]))
    print v

