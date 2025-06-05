# Create a Python program to demonstrate a race condition using multiple threads incrementing a
# shared counter and a mutex to resolve it.

import threading

# shared counter
counter = 0

# Function to increment counter without synchronization
def increment_unsafe():
    global counter
    for _ in range(10000):
        counter += 1

# Function to increment counter with synchronization
def increment_safe(lock):
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

# Demonstrate race condition
threads = [threading.Thread(target=increment_unsafe) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print("Counter without lock:", counter)

# Reset and resolve race condition
counter = 0
lock = threading.Lock()
threads = [threading.Thread(target=increment_safe, args=(lock,)) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print("Counter with lock:", counter)

"""
Explanation
This program demonstrates a race condition by incrementing a shared counter using multiple threads without synchronization, leading to inconsistent results

It then resolves the race condition by synchronizing the operation with a mutex, ensuring that concurrent threads increment the counter consistently and correctly.
"""