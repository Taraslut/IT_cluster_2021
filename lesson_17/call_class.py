class A:
    def __init__(self, x=2):
        self.x = x

    def __call__(self, z, *args, **kwargs):
        return A(z)

a = A()
print(a.x)

b = a(10)
print(b.x)
print(id(a), id(b))