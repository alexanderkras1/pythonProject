from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        """Упрощает дробь"""
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        den = self.b * other.b
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.a * other.a
        den = self.b * other.b
        return Fraction(num, den)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


# Тестирование
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c  # True
assert f_d != f_e  # True
assert f_a == Fraction(2, 3)  # True

print("OK")
