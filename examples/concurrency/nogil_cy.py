import threading
from primes_cy import find_primes, set_stop_requested

def main():
    input("Press Enter to start...\n")

    # Start the prime-finding threads
    threads = []
    for _ in range(6):
        thread = threading.Thread(target=find_primes)
        thread.start()
        print("This line should print, but it is not")
        threads.append(thread)

    try:
        # Keep the main program running for a few seconds
        input("Press Enter to stop...\n")
    finally:
        # Set the event to stop the threads
        set_stop_requested()
        for thread in threads:
            thread.join()   # Wait for the prime threads to finish

    input("Press Enter to exit...\n")

if __name__ == "__main__":
    main()