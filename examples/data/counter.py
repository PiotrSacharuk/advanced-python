from collections import Counter

# List of items
items = ['apple', 'orange', 'banana', 'orange', 'banana', 'banana']

# Create a Counter from the list
item_counter = Counter(items)

# Print the count of each item
print("Item counts:", item_counter)

# Most common item
print("Most common item:", item_counter.most_common(1))