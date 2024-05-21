import threading
import numpy as np
from numba import jit

# Use a NumPy array as a global stop flag
stop_requested = np.array([0], dtype=np.int32)

@jit(nopython=True, nogil=True)
def find_primes(stop_requested):
    num = 2
    while not stop_requested[0]:
        if is_prime(num):
            pass
            # print(f"Prime found: {num}")  # Print directly, manage output issues if arise
        num += 1

@jit(nopython=True, nogil=True)
def is_prime(num):
    """Returns True if num is a prime number, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # prange can be used here safely
        if num % i == 0:
            return False
    return True

def set_stop_requested():
    global stop_requested
    stop_requested[0] = 1

def main():
    input("Press Enter to start...\n")

    # Start the prime-finding threads
    threads = []
    for _ in range(6):
        thread = threading.Thread(target=find_primes, args=(stop_requested,))
        thread.start()
        threads.append(thread)

    input("Press Enter to stop...\n")

    # Signal to stop the threads
    set_stop_requested()

    for thread in threads:
        thread.join()  # Wait for the prime threads to finish

    input("Press Enter to exit...\n")

if __name__ == "__main__":
    main()
