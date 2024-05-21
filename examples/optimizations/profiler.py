import cProfile
from performance import fibonacci, is_prime

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


def compute_operations():
    # Calculate Fibonacci numbers
    fib_numbers = [fibonacci(i) for i in range(35)]  # Increase range for more extensive profiling

    # Check prime status for the first 100 numbers
    prime_status = [is_prime(i) for i in range(50000)]  # Increase range for more extensive profiling

    print("Fibonacci Numbers", fib_numbers)
    print("Prime Status:", prime_status)


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    compute_operations()
    profiler.disable()
    profiler.print_stats(sort='time')
