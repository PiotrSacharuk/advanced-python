import time

def fetch_data(simulated_delay):
    """Simulate a blocking 'API call' with a delay."""
    print(f"Fetching data with a delay of {simulated_delay} seconds...")
    time.sleep(simulated_delay)
    return f"Data fetched after {simulated_delay} seconds"

def main():
    start_time = time.time()
    # Simulate three sequential API calls
    result1 = fetch_data(2)
    print(result1)

    result2 = fetch_data(2)
    print(result2)

    result3 = fetch_data(2)
    print(result3)

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()