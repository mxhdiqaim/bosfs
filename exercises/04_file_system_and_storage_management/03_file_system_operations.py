"""
Explanation
This code snippet defines a simple simulation of basic file system operations in Python

It initializes a root directory and allows creating a file in specified directories

It also implements a function to list all files in a directory.
"""

class FileSystem:
    def __init__(self):
        self.directories = {"/": []}

        print(f"self.directories: {self.directories}")

    def create_file(self, directory, filename):
        print("Creating file...")
        # Check if directory exist
        if directory in self.directories:
            self.directories[directory].append(filename)
        else:
            print(f"Directory {directory} does not exist.")
        
    def list_files(self, directory):
        # List all files in the directory
        return self.directories.get(directory, [])

# Example usage
fs = FileSystem()
fs.create_file("/", "example.txt")
fs.create_file("/", "data.csv")
fs.create_file("/", "image.png")
print(fs.list_files("/"))  # Output: ['example.txt', 'data.csv', 'image.png']