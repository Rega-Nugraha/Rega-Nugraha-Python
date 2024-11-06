class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, y):
        super().__init__(y)
        self.y = y

obj = B(5+9)
print(obj.x)