import ctypes
from ctypes import c_int, POINTER

# Load the shared library
lib = ctypes.CDLL("./libprimes.so")

# Define the function prototype
lib.finder.argtypes = [c_int, POINTER(c_int)]
lib.finder.restype = None

amount = 20000
primes_array = (c_int * amount)()
lib.finder(amount, primes_array)
print(len(primes_array))
