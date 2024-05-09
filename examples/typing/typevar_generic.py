from typing import TypeVar, Generic

# Define a TypeVar, T, which can be any type
T = TypeVar('T')


class Container(Generic[T]):
    """A simple generic container class that can store and retrieve items of any specified type."""

    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        """Return the item stored in the container."""
        return self.item

    def update_item(self, new_item: T) -> None:
        """Update the item stored in the container with a new item of the same type."""
        self.item = new_item
        print(f"Item updated to: {self.item}")


# Example usage with int
int_container = Container[int](300)
print("Initial int:", int_container.get_item())
int_container.update_item(456)

# Example usage with str
str_container = Container[str]("Hello")
print("Initial str:", str_container.get_item())
str_container.update_item("World")

# Example usage with list
list_container = Container[list]([1, 2, 3])
print("Initial list:", list_container.get_item())
list_container.update_item([4, 5, 6])
