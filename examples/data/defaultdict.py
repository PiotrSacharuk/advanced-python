grouped_data = {}

data = [
    ('John', 'Group A'),
    ('Doe', 'Group B'),
    ('Jane', 'Group A'),
    ('Doe', 'Group A')
]

for name, group in data:
    grouped_data[group].append(name)

print("Grouped Data:", dict(grouped_data))
