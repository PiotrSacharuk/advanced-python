def get_lines():
    with open("zenofpython.txt", 'r') as f:
        for line in f.readlines():
            yield line
    print("File closed")

my_iterator = get_lines()

for x in my_iterator:
    print(x)
print("End of file")