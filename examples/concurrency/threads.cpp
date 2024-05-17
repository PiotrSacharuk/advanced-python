#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include <cmath>

// Global stop signal
std::atomic<bool> stop_requested(false);

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= std::sqrt(num); ++i) {
        if (num % i == 0) return false;
    }
    return true;
}

void find_primes(std::atomic<int>& counter) {
    int num = 2;
    while (!stop_requested.load()) {
        if (is_prime(num)) {
            std::cout << "Prime found: " << num << std::endl;
            counter.fetch_add(1, std::memory_order_relaxed);
        }
        num += 1;  // Move to the next number
    }
}

int main() {
    std::cout << "Press Enter to start...\n";
    std::cin.get();
    int num_threads = 4;
    std::vector<std::thread> threads;
    std::atomic<int> prime_count = 0;

    // Start prime-finding threads
    for (int i = 0; i < num_threads; ++i) {
        threads.push_back(std::thread(find_primes, std::ref(prime_count)));
    }

    // Wait for a stop command
    std::cout << "Press Enter to stop...\n";
    std::cin.get();
    stop_requested.store(true);

    // Join all threads
    for (auto& thread : threads) {
        thread.join();
    }
    std::cout << "Press Enter to exit...\n";
    std::cin.get();
    return 0;
}

// Compile with g++ -pthread threads.cpp
