# Write a multi-threaded Python program that simulates a restaurant kitchen, 
# demonstrating safe sharing of resources like an 'oven' using locks for synchronization.

import threading

# Define a lock for synchronizing access to shared resources
oven_lock = threading.Lock()

# Function that a chef thread will run
def use_oven(chef_name):
    print(f'{chef_name} is waiting to use the oven.')

    with oven_lock:
        print(f'{chef_name} is using the oven.')

    # Simulating oven use
    threading.Event().wait(1)
    print(f'{chef_name} has finished using the oven.')


# Creating chef threads
chefs = [threading.Thread(target=use_oven, args=(f'Chef {i}',)) for i in range(3)]

# Start chef threads
for chef in chefs:
    chef.start()

# Wait for all chefs to finish
for chef in chefs:
    chef.join()

"""
Explanation
This code demonstrates a basic use of Python's threading and synchronization tools

We simulate chefs in a kitchen, each needing to use a shared resource, the 'oven'

A lock ensures only one chef uses the oven at a time, preventing race conditions

We create and start multiple threads representing chefs, ensuring they access the shared 'oven' safely using a lock.
"""