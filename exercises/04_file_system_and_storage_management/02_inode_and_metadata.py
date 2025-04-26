"""
Explanation
This code simulates retrieving file information using an inode number in a Unix-like file system

It includes a `FileSystem` class with a static method `retrieve_file` that takes an inode number, 
fetches the corresponding file's metadata and content if the inode exists and prints them.
"""

class FileSystem:
    # Simulated inodes: inode_number -> (filename, metadata, data)
    inodes = {
        1: ('example.txt', {'size': '1KB', 'owner': 'user'}, 'Hello, world!'),
        2: ('data.csv', {'size': '2KB', 'owner': 'user'}, 'id,name,age\n1,Alice,30'),
        3: ('image.png', {'size': '500KB', 'owner': 'user'}, 'binary data here'),
        4: ('video.mp4', {'size': '5MB', 'owner': 'user'}, 'binary data here'),
        5: ('document.pdf', {'size': '1MB', 'owner': 'user'}, 'binary data here'),
        6: ('presentation.pptx', {'size': '2MB', 'owner': 'user'}, 'binary data here'),
        7: ('archive.zip', {'size': '10MB', 'owner': 'user'}, 'binary data here'),
        8: ('script.py', {'size': '3KB', 'owner': 'user'}, 'print("Hello, world!")'),
        9: ('notes.txt', {'size': '512B', 'owner': 'user'}, 'Meeting notes here'),
        10: ('config.json', {'size': '256B', 'owner': 'user'}, '{"key": "value"}'),
        11: ('backup.bak', {'size': '20MB', 'owner': 'user'}, 'binary data here'),
    }

    @staticmethod
    def retrieve_node(inode_number):
        print(f"Retrieving file info for inode number: {inode_number}")
        # fetch file info using inode number
        file_info = FileSystem.inodes.get(inode_number)
        print(f"File info: {file_info}")
        if file_info:
            filename, metadata, data = file_info
            print(f"Filename: {filename}")
            print(f"Metadata: {metadata}")
            print(f"Data: {data}")
        else:
            print("File not found.")
        
    # create a new inode
    @staticmethod
    def create_node(inode_number, filename, metadata, data):
        print(f"Creating file with inode number: {inode_number}")
        FileSystem.inodes[inode_number] = (filename, metadata, data)
        print(f"File created: {FileSystem.inodes[inode_number]}")
    
    # delete an inode

# Example usage
inode_number = 4
FileSystem.retrieve_node(inode_number)
FileSystem.create_node(12, 'newfile.txt', {'size': '1KB', 'owner': 'user'}, 'New file data here')
