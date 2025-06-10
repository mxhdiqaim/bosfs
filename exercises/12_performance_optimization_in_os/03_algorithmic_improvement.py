# Implement a function that simulates a basic Round Robin (RR) CPU scheduling 
# algorithm given a list of process execution times and a time slice.

def round_robin_scheduling(process_times, time_slice):
    # Initialize time and queue of processes
    time = 0
    queue = [(i, t) for i, t in enumerate(process_times)]
    completion_times = [0] * len(process_times)

    # Process queue until empty
    while queue:
        index, remaining_time = queue.pop(0)
        if remaining_time > time_slice:
            # Allocate a time slice, add back to queue
            time += time_slice
            queue.append((index, remaining_time - time_slice))
        else:
            # Process completes
            time += remaining_time
            completion_times[index] = time
            return completion_times

# Example usage
print(round_robin_scheduling([5, 15, 10], 5))

"""
Explanation
The function simulates a basic Round Robin scheduling algorithm

It uses a queue to manage CPU allocation for each process

Each process is given a certain time slice; if the process does not finish execution within this time, it is added back to the queue with its remaining time


"""