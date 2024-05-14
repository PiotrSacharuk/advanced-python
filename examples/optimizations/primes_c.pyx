DEF MAX_SIZE = 1000000

def finder(int amount):

    cdef int found, number, x
    cdef int[MAX_SIZE] primes

    amount = min(amount, MAX_SIZE)
    
    found = 0
    number = 2

    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break
        else:
            primes[found] = number
            found += 1
        number += 1
    
    return [p for p in primes[:found]]