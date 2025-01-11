import sys
import time
import numpy as np
import seq_optimizer

from algorithm import _find_longest_common_sequence
from utils import generate_expect_output, generate_input_data

def benchmark_algorithm(input_data, algorithm):
    """
    Benchmark the algorithm with the specified number of threads.
    """
    start_time = time.time()

    results = algorithm(input_data)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, results

if __name__ == "__main__":
    lengths = [int(1e3), int(1e4), int(1e5), int(1e6), int(1e7)]
    scientific_lengths = [f"{length:.0e}" for length in lengths]
    overlapping = 10

    throughputs = []
    algorithm=seq_optimizer.longest_common
    # algorithm=_find_longest_common_sequence
    for i, length in enumerate(lengths):
        sub_list_count = int(0.1 * length)
        input_data = generate_input_data(length, sub_list_count, overlapping)
        expect_output = generate_expect_output(length)
        
        execution_time, results = benchmark_algorithm(input_data, algorithm)

        total_tokens = sum(list(map(len, input_data)))
        throughput = total_tokens / execution_time
        throughputs.append(throughput)
        
        # Verify correctness
        print(f"Tokens: {scientific_lengths[i]}, Time: {execution_time:.2f}s, \
            Throughput: {throughput:.2f} Tokens/s, \
            Correctness: {np.equal(expect_output, results).all()}")