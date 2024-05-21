import multiprocessing

def is_prime(num):
    """Returns True if num is a prime number, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(stop_event):
    num = 2
    while not stop_event.is_set():
        if is_prime(num):
            print(f"Prime found: {num}")
        num += 1

def main():
    input("Press Enter to start...\n")
    # Create an event to signal the process to stop
    stop_event = multiprocessing.Event()

    num_processes = multiprocessing.cpu_count()

    # Start the prime-finding processes
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=find_primes, args=(stop_event,))
        p.start()
        processes.append(p)

    try:
        # Keep the main program running until Enter is pressed
        input("Press Enter to stop...\n")
    finally:
        # Set the event to stop the processes
        stop_event.set()
        for p in processes:
            p.join()  # Wait for the prime processes to finish

    input("Press Enter to exit...\n")

if __name__ == "__main__":
    main()
