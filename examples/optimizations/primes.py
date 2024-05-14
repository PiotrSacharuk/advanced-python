from typing import List

def finder(amount: int) -> List[int]:
    primes = []
    found = 0
    number = 2

    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break
        else:
            primes.append(number)
            found += 1
        number += 1
    
    return primes