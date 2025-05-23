"""
Explanation
This code simulates a context switch in an operating system with a simple queue of processes

It demonstrates saving the current process's state and switching to the next by rotating the list of processes

This highlights the overhead in context switching and simulates the operation succinctly.
"""

# Simulate a queue of processes by their IDs
process_queue = [1, 2, 3, 4, 5]
# function to simulate context switching
def context_switch(current_process, process_queue):
    # Log saving the state of the current process
    print(f"Saving state of process {current_process}")
    # Rotate the queue to switch to the next process
    process_queue.append(process_queue.pop(0))
    new_process = process_queue[0]
    # Log loading the state of the new process
    print(f"Loading state of process {new_process}")

# Example of simulating context switching
current_process = process_queue[0]
context_switch(current_process, process_queue)
context_switch(process_queue[0], process_queue)

print(f"Current process queue: {process_queue}")