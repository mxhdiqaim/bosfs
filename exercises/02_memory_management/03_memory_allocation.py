# I added print statements to the first_fit function to trace the allocation process.
def first_fit(memory_blocks, process_size):
    allocation = [-1] * len(memory_blocks)
    print("allocation:", allocation)
    # Iterate over each process
    for i, process_size in enumerate(memory_blocks):
        # Try to find a memory block for the process
        print(f"Process i={i} with size {process_size}")
        for j, block_size in enumerate(memory_blocks):
            print(f"Process j={j} with size {block_size}")
            if block_size >= process_size:
                # Allocate block j to process i
                allocation[i] = j
                # Reduce available block size
                memory_blocks[j] -= process_size
                break
    return allocation


# Example usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]
allocation = first_fit(memory_blocks, process_sizes)