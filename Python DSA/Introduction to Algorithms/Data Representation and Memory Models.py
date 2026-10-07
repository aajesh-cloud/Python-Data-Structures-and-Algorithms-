import sys
a = 10
b = 'X'
c = 3.14
d = True
print("Size of int:", sys.getsizeof(a), "bytes")
print("Size of char:", sys.getsizeof(b), "bytes")
print("Size of float:", sys.getsizeof(c), "bytes")
print("Size of bool:", sys.getsizeof(d), "bytes")
print("Address of a:", id(a))