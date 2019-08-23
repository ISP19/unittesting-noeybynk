import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(-5, 7)
        self.assertEqual("-5/7", f.__str__())
        f = Fraction(50, 100)
        self.assertEqual("1/2", f.__str__())
        f = Fraction(420, 12)
        self.assertEqual("35", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(18,0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-33,0)
        self.assertEqual("-1/0", f.__str__())

    # def test_error_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         Fraction(0,0)
    #     with self.assertRaises(ZeroDivisionError):
    #         Fraction(0)/Fraction(0)

    def test_error_value(self):
        with self.assertRaises(ValueError):
            Fraction("A", "a")
        with self.assertRaises(TypeError):
            Fraction("6", [1])


    def test_init(self):
        f = Fraction(5, 10)
        self.assertEqual(1, f.numerator)
        self.assertEqual(2, f.denominator)
        g = Fraction(-2, 0)
        self.assertEqual(-1, g.numerator)
        self.assertEqual(0, g.denominator)
        p = Fraction(-80, 2)
        self.assertEqual(-40, p.numerator)
        self.assertEqual(1, p.denominator)
        q = Fraction(-11,-15)
        self.assertEqual(11, q.numerator)
        self.assertEqual(15, q.denominator)
        r = Fraction(0)
        self.assertEqual(0, r.numerator)
        self.assertEqual(1, r.denominator)
        s = Fraction(60, -90)
        self.assertEqual(-2, s.numerator)
        self.assertEqual(3, s.denominator)
        t = Fraction(5,0)
        self.assertEqual(1, t.numerator)
        self.assertEqual(0, t.denominator)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(329,295), Fraction(30,150)+Fraction(54,59))
        self.assertEqual(Fraction(13,10), Fraction(8,10)+Fraction(7,14))
        self.assertEqual(Fraction(0), Fraction(9,8)+Fraction(-9,8))
        self.assertEqual(Fraction(7,3), Fraction(4,3)+Fraction(1))

    def test_sub(self):
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(10), Fraction(0)-Fraction(100,-10))
        self.assertEqual(Fraction(9,4), Fraction(9,8)-Fraction(-9,8))
        self.assertEqual(Fraction(-1), Fraction(4,5)-Fraction(9,5))
        self.assertEqual(Fraction(83,88), Fraction(20,11)-Fraction(7,8))

    def test_mul(self):
        self.assertEqual(Fraction(1), Fraction(4,5)*Fraction(5,4))
        self.assertEqual(Fraction(1,4), Fraction(5,6)*Fraction(3,10))
        self.assertEqual(Fraction(8,15), Fraction(-2,3)*Fraction(4,-5))
        self.assertEqual(Fraction(0), Fraction(10,986)*Fraction(0))

    def test_div(self):
        self.assertEqual(Fraction(1,2), Fraction(6,2)/Fraction(12,2))
        self.assertEqual(Fraction(1), Fraction(5,10)/Fraction(1,2))
        self.assertEqual(Fraction(0), Fraction(0)/Fraction(123))
        self.assertEqual(Fraction(-8,5), Fraction(2,-5)/Fraction(1,4))

    def test_neg(self):
        self.assertEqual(Fraction(1,4), -Fraction(-25,100))
        self.assertEqual(Fraction(0), -Fraction(0,55))
        self.assertEqual(Fraction(-2,3), -Fraction(2,3))
        self.assertEqual(Fraction(-4), -Fraction(12,3))


    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        a = Fraction(12,0)
        b = Fraction(-12,0)
        c = Fraction(3,0)
        self.assertFalse(a == b)
        self.assertTrue(a.__eq__(c))
        self.assertTrue(Fraction(100,0) == c)
        self.assertFalse(Fraction(100,0) == b)
