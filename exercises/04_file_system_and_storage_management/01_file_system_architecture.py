"""
Explanation
The function 'calculate_blocks' computes the total number of disk blocks needed for a given file size and block size

It calculates how many complete blocks are required and adds an additional block if there is any remainder.
"""

def calculate_block(file_size, block_size):
    # Calculate the number of complete blocks
    complete_blocks = file_size // block_size
    # Determine if there is any remainder that requires an another block 
    if file_size % block_size > 0:
        complete_blocks += 1

    return complete_blocks
    
# Example usage
file_size = 1025  # in bytes
block_size = 512  # in bytes
blocks_needed = calculate_block(file_size, block_size)
print(f"Number of blocks needed: {blocks_needed}")