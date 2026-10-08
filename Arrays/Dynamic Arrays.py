import sys

numbers = []

for i in range(10):
    numbers.append(i)
    print("Size:", len(numbers), ", Internal bytes used:", sys.getsizeof(numbers))