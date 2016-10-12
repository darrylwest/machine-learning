"""Plane class"""

from decimal import Decimal, getcontext

from lib.Vector import Vector

getcontext().prec = 30

class Plane(object):
    """Plane class"""

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        """normal vector [A, B, C] and the constant k"""
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            self.normal_vector = Vector(all_zeros)
        else:
            self.normal_vector = Vector(normal_vector)

        if not constant_term:
            constant_term = Decimal('0')

        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        """set the line's basepoint"""

        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as ex:
            if str(ex) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise ex

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            """write the coefficient"""

            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [
                write_coefficient(n[i], \
                is_initial_term=(i == initial_index)) + 'x_{}'.format(i+1) \
                for i in range(self.dimension) \
                if round(n[i], num_decimal_places) != 0
            ]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def calc_y_intercept(self):
        """calculate the y value for the x @ 0"""
        m = self.constant_term / self.normal_vector.coordinates[1]

        y = self.normal_vector.coordinates[1] * m

        return y

    @staticmethod
    def first_nonzero_index(iterable):
        """find and return the first nonzero index"""

        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k

        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel_to(self, plane):
        """determine if self is parallel to vector using normal"""
        return self.normal_vector.is_parallel_to(plane.normal_vector)

    def __eq__(self, plane):
        if self.normal_vector.is_zero():
            if not plane.normal_vector.is_zero():
                return False
            else:
                return MyDecimal(self.constant_term - plane.constant_term).is_near_zero
        elif plane.normal_vector.is_zero():
            return False

        if not self.is_parallel_to(plane):
            return False

        A = self.basepoint
        B = plane.basepoint

        diff = A.minus(B)

        return diff.is_orthogonal_to(self.normal_vector)

class MyDecimal(Decimal):
    """my decimal helper returns true/false if less than eps"""
    def is_near_zero(self, eps=1e-10):
        """is near zero"""
        return abs(self) < eps
