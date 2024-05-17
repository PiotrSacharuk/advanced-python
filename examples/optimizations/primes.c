#include <stdio.h>
#include <stdlib.h>

void finder(int amount, int *primes) {
    int found = 0;
    int number = 2;
    int is_prime, i;

    while (found < amount) {
        is_prime = 1;
        for (i = 0; i < found; i++) {
            if (number % primes[i] == 0) {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) {
            primes[found++] = number;
        }
        number++;
    }
}

// gcc -shared -fpic -o libprimes.so primes.c

