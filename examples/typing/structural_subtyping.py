from typing import List, TypeVar, Generic, Protocol

T = TypeVar('T')


class StorageProtocol(Protocol[T]):
    def store(self, item: T) -> None:
        ...

    def retrieve(self) -> T:
        ...


class DataStorage(Generic[T], StorageProtocol[T]):
    def __init__(self):
        self.container: List[T] = []

    def store(self, item: T) -> None:
        self.container.append(item)
        print(f"Stored: {item}")

    def retrieve(self) -> T:
        return self.container.pop(0)


# For integers
int_storage = DataStorage[int]()
int_storage.store(123)
print("Retrieved integer:", int_storage.retrieve())

# For strings
str_storage = DataStorage[str]()
str_storage.store("Hello, world!")
print("Retrieved string:", str_storage.retrieve())


class BatchDataStorage(DataStorage[T]):
    def store_multiple(self, items: List[T]) -> None:
        for item in items:
            self.store(item)

    def retrieve_all(self) -> List[T]:
        items = []
        while self.container:
            items.append(self.retrieve())
        return items


# Using BatchDataStorage
batch_storage = BatchDataStorage[str]()
batch_storage.store_multiple(["data1", "data2", "data3"])
print("Retrieved all items:", batch_storage.retrieve_all())
