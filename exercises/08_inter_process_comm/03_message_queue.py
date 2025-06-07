# Implement a basic message queue system using the 'queue' module in Python,
# with one producer and one consumer process, using the 'multiprocessing' library.

import multiprocessing
import time
import queue

# function for producer process

def producer(q):
    for i in range(5):
        item = f"Message {i}"
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(1) # Simulate production delay

# Function for consumer process
def consumer(q):
    while True:
        # Try to get a message and process it
        try:
            item = q.get(timeout=2)
            print(f"Consumed: {item}")
            time.sleep(2) # Simulate consumption delay
        except queue.Empty:
            break # Exit if no more messages

if __name__ == "__main__":
    q = multiprocessing.Queue()
    prod = multiprocessing.Process(target=producer, args=(q,))
    cons = multiprocessing.Process(target=consumer, args=(q,))
    prod.start()
    cons.start()
    prod.join()
    cons.join()

"""
Explanation
This code snippet demonstrates the implementation of a basic message queue using Python's 'queue' and 'multiprocessing' libraries

A producer process creates and enqueues messages in a shared queue, simulating production delays, while a consumer process dequeues and processes these messages, simulating consumption delays

The example showcases asynchronous message handling and how the system manages different processing speeds.
"""