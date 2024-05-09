# Coding Challenge: Custom Dictionary-Like Object

## Background:
Python provides the dict type for storing key-value pairs. This challenge involves creating a custom class that mimics the behavior of a dictionary by overriding the relevant dunder methods, such as __getitem__, __setitem__, __delitem__, __contains__, and __iter__.

## Challenge Description:
You are tasked with writing a class named CustomDict that behaves like a dictionary. This class should store its data in a private attribute and expose dictionary-like behavior through overridden dunder methods.

## Requirements:
Implement a class named CustomDict that behaves like a dictionary.
Store the key-value pairs in a private dictionary attribute.
Override the following dunder methods to provide dictionary-like behavior:
```
__getitem__(self, key): Returns the value associated with the key.
__setitem__(self, key, value): Sets the value for a given key.
__delitem__(self, key): Removes the key-value pair for a given key.
__contains__(self, key): Checks if a key is in the dictionary.
__iter__(self): Returns an iterator over the dictionary's keys.
__len__(self): Returns the number of key-value pairs.
__repr__(self): Provides a string representation of the object.
```

Example Usage:

```
cd = CustomDict()
cd['a'] = 1
cd['b'] = 2

print("CustomDict:", cd)
print("'a' in CustomDict:", 'a' in cd)
print("Keys in CustomDict:", list(cd))
print("Number of items in CustomDict:", len(cd))

del cd['a']
print("After deleting 'a':", cd)
```

Expected Output:
```
CustomDict: {'a': 1, 'b': 2}
'a' in CustomDict: True
Keys in CustomDict: ['a', 'b']
Number of items in CustomDict: 2
After deleting 'a': {'b': 2}
```

## Instructions:
1. Implement the CustomDict class and override the specified dunder methods to mimic dictionary behavior.
2. Test the class using the provided example usage to ensure it behaves like a dictionary.
3. Add additional tests to check edge cases such as attempting to access a non-existent key.

## Goals of the Challenge:
* Practice overriding dunder methods to customize the behavior of a Python class.
* Understand how to implement dictionary-like behavior in custom classes.
* Learn about handling key-value data with custom methods and attributes.
