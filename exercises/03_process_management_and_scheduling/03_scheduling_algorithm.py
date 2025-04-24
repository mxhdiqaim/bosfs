"""
Explanation
The code simulates the FCFS scheduling algorithm

It computes waiting time for each process based on the sum of burst times of all previous processes

Then, it calculates the average waiting time by dividing the total waiting time by the number of processes.
"""

def fcfs_scheduling(processes):
    waiting_time = [0] * len(processes) # Initialize waiting time array [0, 0, 0]
    print("waiting_time:", waiting_time)
    total_waiting_time = 0 # Initialize total waiting time 
    
    # Calculate waiting time for each process
    for i in range(1, len(processes)):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1]
        total_waiting_time += waiting_time[i]
    
    # Calculate average waiting time
    average_waiting_time = total_waiting_time / len(processes)
    return average_waiting_time
    
# Example usage
processes = [24, 3, 3]  # Burst times
average_waiting_time = fcfs_scheduling(processes)
print(f"Average waiting time: {average_waiting_time} units")
# This code simulates the First-Come, First-Served (FCFS) scheduling algorithm
# It calculates the average waiting time for a list of processes based on their burst times