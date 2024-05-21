import asyncio

async def fetch_data(simulated_delay):
    """Simulate a non-blocking 'API call' with a delay."""
    print(f"Fetching data with a delay of {simulated_delay} seconds...")
    await asyncio.sleep(simulated_delay)
    return f"Data fetched after {simulated_delay} seconds"

async def main():
    start_time = asyncio.get_event_loop().time()

    # Schedule three concurrent API calls
    task1 = fetch_data(2)
    task2 = fetch_data(2)
    task3 = fetch_data(2)

    results = await asyncio.gather(task1, task2, task3)
    for result in results:
        print(result)

    end_time = asyncio.get_event_loop().time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
