class CustomDict:
    pass

# Example usage:
cd = CustomDict()
cd['a'] = 1
cd['b'] = 2

print("CustomDict:", cd)
print("'a' in CustomDict:", 'a' in cd)
print("Keys in CustomDict:", list(cd))
print("Number of items in CustomDict:", len(cd))

del cd['a']
print("After deleting 'a':", cd)