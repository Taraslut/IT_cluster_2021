class Circle:
    pi = 3.1415

    def __init__(self, R):
        self.R = R

    @property
    def d(self):
        return 2 * self.R

    @staticmethod
    def power2(x):
        return x * x

    @classmethod
    def by_diameter(cls, d):
        return cls(d / 2)


c = Circle(12)

print(c.R)
print(c.d)
print(Circle.__dict__)
print(c.pi)
print(Circle.pi)

print(c.power2(10))

print(Circle.power2(3))

ss = Circle.by_diameter(100)
print(ss.R)

print(ss)