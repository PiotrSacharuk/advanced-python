class MetaClass(type):
    def __new__(*args, **kwargs):
        return super().__new__(*args, **kwargs)

class MyClass(metaclass=MetaClass):
    def __init__(self):
        self.x = 2
    def update(self, x):
        self.x = x
        print(f"New value is {x}")

a = MyClass()
a.update(5)