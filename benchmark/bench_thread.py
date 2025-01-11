import sys
import time
import numpy as np
import seq_optimizer

from concurrent.futures import ThreadPoolExecutor

from algorithm import _find_longest_common_sequence
from utils import generate_expect_output, generate_input_data

def benchmark_algorithm(input_data, algorithm, thread_count):
    """
    Benchmark the algorithm with the specified number of threads.
    """
    start_time = time.time()

    def worker(data_chunk):
        return algorithm(data_chunk)

    # Split data into chunks for threading
    chunk_size = len(input_data) // thread_count
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    # Run algorithm with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        results = list(executor.map(worker, chunks))

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, results

if __name__ == "__main__":
    length = int(1e7)
    sub_list_count = int(1e5)
    overlapping = 10

    input_data = generate_input_data(length, sub_list_count, overlapping)
    expect_output = generate_expect_output(length)
    
    print(f"has sub-sequences: {len(input_data)}")
    print(f"all tokens: {sum(list(map(len, input_data)))}")

    thread_counts = [1, 2, 4, 8, 16]
    throughputs = []
    # algorithm=seq_optimizer.longest_common
    algorithm=_find_longest_common_sequence
    for thread_count in thread_counts:
        execution_time, results = benchmark_algorithm(input_data, algorithm, thread_count)
        result = results[0]
        for i in range(1, len(results)):
            next_seq = results[i][overlapping:]
            result = np.concatenate([result, next_seq])
        
        # Calculate throughput in MB/s
        data_size_mb = (length * 4) / (1024 ** 2)  # Each integer is 4 bytes
        throughput = data_size_mb / execution_time
        throughputs.append(throughput)
        
        # Verify correctness
        print(f"Threads: {thread_count}, Time: {execution_time:.2f}s, \
            Throughput: {throughput:.2f} MB/s, \
            Correctness: {np.equal(expect_output, result).all()}")