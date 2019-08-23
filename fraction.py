import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """

        if numerator == 0 and denominator == 0:
            self.numerator = numerator
            self.denominator = denominator
        else:
            div = math.gcd(int(numerator), int(denominator))
            numerator /= div
            denominator /= div

        if denominator == 0 and numerator >=1:
            self.numerator = 1
            self.denominator = 0
        elif denominator == 0 and numerator <=-1:
            self.numerator = -1
            self.denominator = 0
        elif numerator>0 and denominator<0:
            self.numerator = -numerator
            self.denominator = -denominator
        elif numerator<0 and denominator<0:
            self.numerator = -numerator
            self.denominator = -denominator
        else:
            self.numerator = numerator
            self.denominator = denominator
    
    def __str__(self):
        # div = math.gcd(int(self.numerator), int(self.denominator))
        # self.numerator /= div
        # self.denominator /= div
        if self.denominator == 1:
            return f"{int(self.numerator)}"
        elif self.denominator == 0 and self.numerator == 0:
            return "0/0"
        return f"{int(self.numerator)}/{int(self.denominator)}"

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator*frac.denominator + self.denominator*frac.numerator)
        denominator = (self.denominator*frac.denominator)
        div = math.gcd(int(numerator), int(denominator))
        numerator /= div
        denominator /= div
        return Fraction(numerator, denominator)

    def __sub__(self, frac):
        numerator = (self.numerator*frac.denominator - self.denominator*frac.numerator)
        denominator = (self.denominator*frac.denominator)
        div = math.gcd(int(numerator), int(denominator))
        numerator /= div
        denominator /= div
        return Fraction(numerator, denominator)
    
    def __mul__(self, frac):
        numerator = self.numerator*frac.numerator
        denominator = self.denominator*frac.denominator
        div = math.gcd(int(numerator), int(denominator))
        numerator /= div
        denominator /= div
        return Fraction(numerator, denominator)
    
    def __truediv__(self, frac):
        numerator = self.numerator*frac.denominator
        denominator = self.denominator*frac.numerator
        div = math.gcd(int(numerator), int(denominator))
        numerator /= div
        denominator /= div
        return Fraction(numerator, denominator)
    
    def __neg__(self):
        if self.numerator>0 and self.denominator>0:
            numerator = -self.numerator
            denominator = self.denominator
        elif self.numerator<0 and self.denominator<0:
            numerator = -self.numerator
            denominator = self.denominator
        elif self.numerator<0 and self.denominator>0:
            numerator = -self.numerator
            denominator = self.denominator
        elif self.numerator>0 and self.denominator<0:
            numerator = self.numerator
            denominator = -self.denominator
        elif self.numerator == 0:
            numerator = 0
            denominator = self.denominator
        return Fraction(numerator,denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        div1 = math.gcd(int(self.numerator),int(self.denominator))
        div2 = math.gcd(int(frac.numerator),int(frac.denominator))
        self.numerator /= div1
        self.denominator /= div1
        frac.numerator /= div2
        frac.denominator /= div2
        if self.numerator == frac.numerator and self.denominator == frac.denominator:
            return True
        else:
            return False


            
# p=Fraction(2,3)
# q=Fraction(-2,3)
# r=Fraction(-2,-3)
# s=Fraction(2,-3)
# print(-p)
# print(-q)
# print(-r)
# print(-s)
