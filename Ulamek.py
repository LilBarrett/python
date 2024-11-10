import math
class Ulamek:
    '''
        Class representing fractions, with comparasions and algebraic operators defined.
        Atributes: numerator (integer), 
                   denominator (integer)
        Methods: __init__,
                 __add__,
                 __sub__,
                 __mul__,
                 __truediv__,
                 __eq__,
                 __ne__,
                 __lt__,
                 __le__,
                 __gt__,
                 __ge__;
    '''
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

def tester(fractions):
    pause = "-------------------------------------------------------------------"
    long_pause = "*******************************************************************"
    for fra_x in fractions:
        for fra_y in fractions:
            print(f"Testing comparasions for {fra_x} and {fra_y}:")
            print(f"{fra_x} = {fra_y} is {fra_x == fra_y}")
            print(f"{fra_x} != {fra_y} is {fra_x != fra_y}")
            print(f"{fra_x} > {fra_y} is {fra_x > fra_y}")
            print(f"{fra_x} < {fra_y} is {fra_x < fra_y}")
            print(f"{fra_x} >= {fra_y} is {fra_x >= fra_y}")
            print(f"{fra_x} >= {fra_y} is {fra_x <= fra_y}")
            print(pause)
            print(f"Testing operators for {fra_x} and {fra_y}:")
            print(f"{fra_x} + {fra_y} is {fra_x + fra_y}")
            print(f"{fra_x} - {fra_y} is {fra_x - fra_y}")
            print(f"{fra_x} * {fra_y} is {fra_x * fra_y}")
            print(f"{fra_x} / {fra_y} is {fra_x / fra_y}")
            print(long_pause)

if __name__ == "__main__":
    a = Ulamek(1, -4)
    b = Ulamek(1, -2)
    c = Ulamek(5, -4)
    d = Ulamek(-7, 2)
    fraction_list = [a, b, c, d]
    tester(fraction_list)
