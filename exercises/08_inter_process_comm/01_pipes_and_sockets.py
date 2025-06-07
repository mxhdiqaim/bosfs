# Demonstrate IPC by implementing a Python program that uses an unnamed pipe to send a message
# from a parent process to a child process, and a simple client-server application using sockets.

# The below code is buggy, I cannot make it to run

import os, socket
from multiprocessing import Process

# Set up pipe
pipe_in, pipe_out = os.pipe()

# Function for child process read from pipe
def child_read(pipe_in):
    os.close(pipe_out) # Close unused write end
    message = os.read(pipe_in, 1024).decode()
    print(f"Child received: {message}")
    os.write(pipe_out, b'Child echo: ' + message.encode())
    os.close(pipe_in)


if os.fork() == 0:
    child_read(pipe_in)
else:
    os.close(pipe_in) # Close unused read end
    os.write(pipe_out, b'Hell from parent')
    response = os.read(pipe_out, 1024).decode()
    print(f"Parent received: {response}")
    os.close(pipe_out)

# Socket server setup
def server():
    s = socket.socket()
    s.bind(('localhost', 12345))
    s.listen(1)
    conn, addr = s.accept()
    conn.sendall(b'Welcome!')
    conn.close()

# Socket client setup
def client():
    s = socket.socket()
    s.connect(('localhost', 12345))
    print(s.recv(1024).decode())
    s.close()

# Run server and client
server_process = Process(target=server)
server_process.start()
client_process = Process(target=client)
client_process.start()
server_process.join()
client_process.join()

"""
Explanation
This code demonstrates two IPC mechanisms: pipes and sockets

The unnamed pipe facilitates communication between a parent and its child process

The parent writes a message to the pipe, which the child reads, echoes back, and the parent then reads this echoed message

The socket code runs a simple server-client architecture, where the server sends a welcome message to the client upon connection

The child and client processes are spawned using multiprocessing for separation.
"""