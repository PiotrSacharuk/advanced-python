import threading

def find_primes(stop_event):
    num = 2
    while not stop_event.is_set():
        if is_prime(num):
            print(f"Prime found: {num}")
        num += 1

def is_prime(num):
    """Returns True if num is a prime number, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    input("Press Enter to start...\n")
    # Create an event to signal the thread to stop
    stop_event = threading.Event()

    # Start the prime-finding threads
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=find_primes, args=(stop_event,))
        thread.start()
        threads.append(thread)

    try:
        # Keep the main program running for a few seconds
        input("Press Enter to stop...\n")
    finally:
        # Set the event to stop the threads
        stop_event.set()
        for thread in threads:
            thread.join()   # Wait for the prime threads to finish

    input("Press Enter to exit...\n")

if __name__ == "__main__":
    main()