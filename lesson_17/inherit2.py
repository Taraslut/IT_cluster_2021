class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.perimeter = 2 * (self.a + self.b)

    @property
    def sq(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f'<{self.__class__.__name__}, a={self.a}, b={self.b}>'


class Square(Rect):
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return f'<{self.__class__.__name__}, a={self.a}>'

r = Rect(2, 3)
print(r.sq)
print(r.perimeter)

r.a = 12
r.b = 24
print(r.perimeter)


s = Square(3)

print(s.sq)
print(s.perimeter)

print(r)
print(s)
