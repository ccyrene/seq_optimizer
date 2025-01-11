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

    print(f"longest sequence: {longest_sequence}")
```

## Performance Comparison
Provide benchmarks and comparisons between Hugging Face's implementation and this optimized Rust version to showcase the speedup.

## License
[MIT](./LICENSE)