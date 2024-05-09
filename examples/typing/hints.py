from typing import List, Dict, Union, Optional, Callable

# Define a type for the entries to make the dictionary hint more descriptive
Entry = Dict[str, Union[str, int, None]]

def process_entries(entries: List[Entry], 
                    transform: Optional[Callable[[Union[str, int]], Union[str, int]]] = None) -> List[Entry]:
    """
    Process a list of entries. Each entry is a dictionary with keys that have values of type str or int.
    Optionally, apply a transformation function to all values.

    :param entries: List of dictionaries with keys as str and values as either str or int.
    :param transform: Optional callable that takes a Union[str, int] and returns Union[str, int].
    :return: A new list of processed dictionaries.
    """
    processed = []
    for entry in entries:
        new_entry = {}
        for key, value in entry.items():
            # Apply transformation if it is not None and the value is not None
            if transform and value is not None:
                new_entry[key] = transform(value)
            else:
                new_entry[key] = value
        processed.append(new_entry)
    return processed

# Example usage:
data: List[Entry] = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25, 'city': 'New York'}
]

# Define a simple transformation function
def to_string(x: Union[str, int]) -> str:
    return str(x)

# Process data
processed_data = process_entries(data, transform=to_string)
print(processed_data)
