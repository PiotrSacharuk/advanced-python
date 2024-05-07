class MyClass:

    def __init__(self):
        self.__x = 0
        self._x = 1
        self.x = 2


a = MyClass()
print(a.__x)