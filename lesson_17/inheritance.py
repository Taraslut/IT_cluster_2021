class A:
    z = 4

    def __init__(self, x):
        self._x = x



a = A(12)
print(a._x)
a._x = 99
print(a._x)
print(a.z)
