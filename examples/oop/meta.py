# Custom metaclass to log class creation and add a method
class LoggedMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        # Add a method to the class dynamically
        dct['greet'] = lambda self: print(f"Hello from {name}")
        instance = super().__new__(cls, name, bases, dct)
        return instance

# Example usage of the LoggedMeta metaclass
class ExampleClass(metaclass=LoggedMeta):

    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

# Creating an instance of ExampleClass
example = ExampleClass(42)
example.display()  # Regular method defined in the class
example.greet()    # Dynamically added by the metaclass
