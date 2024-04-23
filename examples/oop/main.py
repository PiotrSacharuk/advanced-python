class MyClass:

    def __init__(self):
        self.__x = 0
        self._x = 1
        self.x = 2


import pdb; pdb.set_trace()
a = MyClass()
print(a.__x)