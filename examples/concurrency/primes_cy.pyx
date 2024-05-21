from libc.math cimport sqrt
from libc.stdio cimport printf

cdef bint stop_requested = 0

cpdef set_stop_requested():
    global stop_requested
    stop_requested = 1

cdef int is_prime(int num) nogil:
    cdef int i
    if num <= 1:
        return 0
    cdef int limit = <int>sqrt(num) + 1
    for i in range(2, limit):
        if num % i == 0:
            return 0
    return 1

cpdef void find_primes() nogil:
    cdef int num = 2
    while not stop_requested:
        if is_prime(num):
            printf("Prime found: %d\n", num)
        num += 1