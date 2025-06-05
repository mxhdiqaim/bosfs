# Simulate multiple threads adding items to a shared shopping cart with synchronization using a
# mutex to prevent race conditions.

from threading import Thread, Lock

# Shared shopping cart and a mutex lock
shopping_cart = []
cart_lock = Lock()
def add_to_cart(item):
    # Acquire the lock before modifying the shared resource
    with cart_lock:
        shopping_cart.append(item)

# Create threads that add items to the cart
threads = [Thread(target=add_to_cart, args=(f"item{i}",)) for i in range(5)]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Output the shopping cart contents
print(shopping_cart)

"""
Explanation
This code demonstrates the use of a mutex (Lock) to synchronize access to a shared shopping cart by multiple threads

Each thread adds an item to the cart, but the lock ensures that only one thread modifies the cart at a time, preventing race conditions.
"""