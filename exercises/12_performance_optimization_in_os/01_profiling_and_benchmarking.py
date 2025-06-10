# Write a function to simulate a simple web application that experiences latency issues. 
# Create an artificial delay in a function and profile it to identify the bottleneck function call.

import time
import cProfile

# Simulated function representing a latency bottleneck
def bottleneck_function():
    time.sleep(2)  # Artificial delay to simulate performance issue
    return 'Finished long task'

def main():
    print(bottleneck_function())
    
# Profile the main function to find the bottleneck
cProfile.run('main.()')

"""
Explanation
The code demonstrates profiling a Python function that simulates a latency issue using an artificial delay

The 'bottleneck_function' simulates a task with a significant delay, representing a performance bottleneck

Using Python's 'cProfile', we analyze the program execution to identify that this function is the major contributor to the latency, thus pinpointing where optimization is necessary.
"""