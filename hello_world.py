import time

def test_cycle_speed(iterations):
    print(f"Testing cycle speed with {iterations} iterations...")
    start_time = time.time()
    
    # Simple loop to iterate through the range
    for i in range(iterations):
        pass  # No operation, just cycling
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    print(f"Iterations per second: {iterations / elapsed_time:.2f}")

# Test with 100 million iterations
test_cycle_speed(1_000_000_000)