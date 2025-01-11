import matplotlib.pyplot as plt
import numpy as np

def plot_thread():
    threads = [1, 2, 4, 8, 16]
    seq_optimizer_throughput = [52.28, 53.37, 54.11, 55.99, 53.89]
    transformers_throughput = [0.18, 0.17, 0.17, 0.18, 0.17]

    plt.figure(figsize=(12, 7))
    bar_width = 0.35

    x_positions = np.arange(len(threads))

    plt.bar(x_positions - bar_width/2, seq_optimizer_throughput, width=bar_width, label='seq_optimizer', color='#ff7f0e', alpha=0.8)
    plt.bar(x_positions + bar_width/2, transformers_throughput, width=bar_width, label='huggingface', color='#65F586', alpha=0.8)

    plt.xlabel('Thread count', fontsize=14)
    plt.ylabel('Throughput (MB/s)', fontsize=14)
    plt.xticks(x_positions, threads, fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0, max(seq_optimizer_throughput) + 10)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, v in enumerate(seq_optimizer_throughput):
        plt.text(x_positions[i] - bar_width/2, v + 1, f"{v:.1f}", ha='center', fontsize=10)
    for i, v in enumerate(transformers_throughput):
        plt.text(x_positions[i] + bar_width/2, v + 1, f"{v:.2f}", ha='center', fontsize=10)

    output_path_equal_spacing = "../perf_thread.svg"
    plt.savefig(output_path_equal_spacing, bbox_inches='tight', dpi=300)
    plt.show()

    print(output_path_equal_spacing)
    
def plot_tokens():
    norm = int(1e4)
    lengths = [int(1e3), int(1e4), int(1e5), int(1e6), int(1e7)]
    scientific_lengths = [f"{length:.0e}" for length in lengths]
    seq_optimizer_throughput = [t / norm for t in [18144923.83, 25384237.65, 23847017.97, 22897182.69, 23302376.31]]
    formatted_seq_optimizer_throughput = [f"{throughput:.2f}e+4" for throughput in seq_optimizer_throughput]
    transformers_throughput = [t / norm for t in [84996.59, 89065.23, 91240.57, 89677.42, 88661.93]]
    formatted_transformers_throughput = [f"{throughput:.2f}e+4" for throughput in transformers_throughput]

    plt.figure(figsize=(12, 7))
    bar_width = 0.35

    x_positions = np.arange(len(scientific_lengths))

    plt.bar(x_positions - bar_width/2, seq_optimizer_throughput, width=bar_width, label='seq_optimizer', color='#ff7f0e', alpha=0.8)
    plt.bar(x_positions + bar_width/2, transformers_throughput, width=bar_width, label='huggingface', color='#65F586', alpha=0.8)

    plt.xlabel('Token count', fontsize=14)
    plt.ylabel('Throughput (Tokens/s)', fontsize=14)
    plt.xticks(x_positions, scientific_lengths, fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0, max(seq_optimizer_throughput) + 1000)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, v in enumerate(seq_optimizer_throughput):
        plt.text(x_positions[i] - bar_width/2, v + 1, formatted_seq_optimizer_throughput[i], ha='center', fontsize=10)
    for i, v in enumerate(transformers_throughput):
        plt.text(x_positions[i] + bar_width/2, v + 1, formatted_transformers_throughput[i], ha='center', fontsize=10)

    output_path_equal_spacing = "../perf_token.svg"
    plt.savefig(output_path_equal_spacing, bbox_inches='tight', dpi=300)
    plt.show()

    print(output_path_equal_spacing)
    
if __name__ == "__main__":
    plot_tokens()
    plot_thread()