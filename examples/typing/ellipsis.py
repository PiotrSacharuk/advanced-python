class CustomContainer:
    def __getitem__(self, item):
        if item is Ellipsis:
            return "Returning all contents"
        return f"Accessing item {item}"

container = CustomContainer()
print(container[...])  # Using Ellipsis to mean "all items" or similar