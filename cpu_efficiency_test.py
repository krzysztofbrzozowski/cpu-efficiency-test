import time
import multiprocessing
from math import sqrt

def find_primes(limit):
    """Find all prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return len(primes)  # Return the count of primes found

def cpu_stress_task(duration, limit):
    """
    Perform CPU-intensive tasks for the given duration and count operations.
    
    Args:
        duration (int): Duration of the task in seconds.
        limit (int): Limit for prime number calculations.
        
    Returns:
        int: Total number of operations completed.
    """
    start_time = time.time()
    operations = 0

    while time.time() - start_time < duration:
        find_primes(limit)
        operations += 1  # Increment the operation count after each run

    return operations

def run_cpu_efficiency_test(duration=10, processes=4, limit=10000):
    """
    Run CPU efficiency test.
    
    Args:
        duration (int): Duration of the test in seconds.
        processes (int): Number of processes to spawn.
        limit (int): Limit for prime number calculations.
    """
    print(f"Starting CPU efficiency test for {duration} seconds using {processes} processes...")
    start_time = time.time()

    # Define the arguments for each process
    args = [(duration, limit) for _ in range(processes)]

    # Create a pool of workers to stress the CPU
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.starmap(cpu_stress_task, args)

    total_operations = sum(results)
    elapsed_time = time.time() - start_time

    efficiency = total_operations / elapsed_time
    print(f"Test completed in {elapsed_time:.2f} seconds.")
    print(f"Total operations completed: {total_operations}")
    print(f"CPU efficiency: {efficiency:.2f} operations per second.")

if __name__ == "__main__":
    run_cpu_efficiency_test(duration=10, processes=4, limit=10000)
