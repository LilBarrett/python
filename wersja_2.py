import random
import math
from time import time
import operator
class Ulamek:
    __slots__ = ('numerator', 'denominator') 
    def __init__(self, numerator, denominator):
        
        assert denominator != 0    # Prevents dividing by zero
        gcd = math.gcd(numerator, denominator)    

        # Change numerator and denominator such that the fraction is irreducible
        self.numerator = numerator//gcd if denominator > 0 else -numerator//gcd   # Sign correction based on denominator sign
        self.denominator = abs(denominator//gcd)    # Set denominator to be positive

    # Define fraction addition
    def __add__(self, other):
        
        num_self = self.numerator
        dem_self = self.denominator
        num_other = other.numerator
        dem_other = other.denominator

        return Ulamek(num_self * dem_other + dem_self * num_other, dem_self*dem_other)

    # Define fraction subtraction
    def __sub__(self, other):
        
        other_neg = Ulamek(-other.numerator, other.denominator)
        return self.__add__(other_neg)

    # Define fraction multiplication
    def __mul__(self, other):
        
        new_num = self.numerator * other.numerator
        new_dem = self.denominator * other.denominator
        
        return Ulamek(new_num, new_dem)

    # Define fraction division
    def __truediv__(self, other):
        
        other_reversed = Ulamek(other.denominator, other.numerator)
        return self.__mul__(other_reversed)

    # Define Fraction comparasions
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator*other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator*other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator*other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator*other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator*other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator*other.numerator

    # Define fraction printing
    def __str__(self):
        if self.numerator == 0:
            return (str(0))
        else:
            return (f"{self.numerator}/{self.denominator}")
            
    def __repr__(self):
        if self.numerator == 0:
            return (str(0))
        else:
            return (f"{self.numerator}/{self.denominator}")
            
    pass

def benchmark(iterations=10**7):
    fractions = [Ulamek(random.randint(-10**6, 10**6), random.randint(1, 10**6))
        for j in range(10**7)]

    operations = [
        (operator.add, '+'),
        (operator.sub, '-'),
        (operator.mul, '*'),
        (operator.lt, '<'),
        (operator.le, '<='),
        (operator.gt, '>'),
        (operator.ge, '>='),
        (operator.eq, '=='),
        (operator.ne, '!=')
    ]

    for i in range(iterations):

        idx1 = random.randint(0, len(fractions)-1)
        idx2 = random.randint(0, len(fractions)-1)
        a = fractions[idx1]
        b = fractions[idx2]

        op, _ = random.choice(operations)

        result = op(a, b)
        if isinstance(result, Ulamek):
            fractions[random.randint(0, len(fractions)-1)] = result

if __name__ == "__main__":
     benchmark()

