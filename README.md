# Sequences Optimization with Rust
This repository is dedicated to optimizing the handling of sequences, particularly those generated as outputs from the Whisper model. The default `find_longest_common_sequence` function from Hugging Face's Transformers library, while effective, can be slow for large or complex sequences. By leveraging Rust's performance capabilities, this project introduces a faster and more efficient implementation of sequence processing.

## Features
- **High-Performance Sequence Optimization:** Faster computation of the longest common subsequence compared to Hugging Face's implementation.
- **Integration with Whisper Outputs:** Specifically tailored for sequence data produced by Whisper.
- **Rust Efficiency:** Written in Rust for improved speed and resource utilization.
- **Seamless Integration:** Easy to integrate into existing workflows involving Hugging Face Transformers.

## Installation
```bash
$pip install seq_optimizer
```

## Usage
```python
import seq_optimizer

sequences = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

longest_sequence = seq_optimizer.longest_common(sequences)

print(f"longest sequence: {longest_sequence}") #expected [1, 2, 3, 4, 5]
```

## Performance Comparison

### Token-Level Performance
![Performance Chart](https://raw.githubusercontent.com/esylenn/seq_optimizer/main/perf_thread.svg)
This chart illustrates the performance of the optimized implementation on a total of 10 million tokens, where each sub-sequence contains 100,000 tokens, overlapping with 10 elements. The results showcase a significant speedup, making this approach highly efficient for large-scale sequence processing.

### Scaling with Total Tokens
![Scaling Performance](https://raw.githubusercontent.com/esylenn/seq_optimizer/main/perf_token.svg)
This chart evaluates the performance as the total number of tokens varies from 1,000 to 10 million. Each sub-sequence contains 10% of the total tokens, with 10 overlapping elements per sub-sequence. The optimized implementation demonstrates consistent scalability and improved efficiency across all token ranges.


## License
[MIT](./LICENSE)