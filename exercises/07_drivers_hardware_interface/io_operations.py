# Implement a buffer system in Python to simulate reading a data block from a device driver,
# where the buffer size is limited and must handle buffer overflow by discarding excess data.

class Buffer:
    def __init__(self, size):
        self.size = size
        self.data = []

    def write(self, block):
        # Append data block to the buffer
        self.data += block

        # Check for overflow and discard excess data
        if len(self.data) > self.size:
            overflow_amount = len(self.data) - self.size
            print(f"Buffer overflow! Discarding {overflow_amount} items.")
            self.data = self.data[-self.size:]

# Example usage
buffer = Buffer(10)
buffer.write([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(buffer.data)  # Output should be [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
Explanation
This code demonstrates a simple buffer system handling data overflow

The Buffer class has a fixed size, and writes to the buffer truncate excess data if it exceeds the defined limit, 
simulating a conceptual model of data management during I/O operations in an operating system.
"""