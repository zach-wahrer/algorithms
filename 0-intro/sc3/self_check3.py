# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n
# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)


class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise Exception("Both numbers for a Fraction must be ints.")
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def show(self):
        print(self.num, "/", self.den)

    # Add new work here

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den - other.den * self.den
        if new_den == 0:
            new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __gt__(self, other):
        self_new_num = self.num * other.den
        other_new_num = other.num * self.den
        return self_new_num > other_new_num

    def __lt__(self, other):
        self_new_num = self.num * other.den
        other_new_num = other.num * self.den
        return self_new_num < other_new_num

    def __ge__(self, other):
        self_new_num = self.num * other.den
        other_new_num = other.num * self.den
        return self_new_num >= other_new_num

    def __le__(self, other):
        self_new_num = self.num * other.den
        other_new_num = other.num * self.den
        return self_new_num <= other_new_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
print(x * y)
print(x / y)
print(x - y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x != y)
print(x.get_num())
print(x.get_den())

z = Fraction("error", 1)
