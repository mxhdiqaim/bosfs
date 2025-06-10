# Implement a FIFO cache replacement policy simulator in Python. Your function should 
# take a list of requests and a cache size, and return the number of cache hits.

def fifo_cache(requests, cache_size):
    cache = []  # Initialize an empty list to represent the cache
    hits = 0
    for request in requests:
        if request in cache:
            hits += 1  # Increment hits if the request is found in cache
        else:
            if len(cache) == cache_size:
                cache.pop(0)  # Remove the oldest item if the cache is full
                cache.append(request)  # Add the new request to the cache
                return hits
            
# Example usage
print(fifo_cache([1, 2, 3, 2, 1, 4, 5], 3))

"""
Explanation
This code simulates a FIFO cache by maintaining a list of recent requests

It checks for cache hits and handles cache replacement when the cache reaches 
its size limit by removing the oldest item.
"""