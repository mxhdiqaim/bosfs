// Write a C program that demonstrates error handling when opening a file in a Linux environment. 
// Handle errors when the file does not exist and when there are insufficient permissions.

#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

int main() {
    int fd;

    // Attempt to open an existing file
    fd = open("example.txt", O_RDONLY);
    if (fd == -1) {
        // Check error if the file does not exist
        if (errno == ENOENT) {
            printf("Error: File does not exist.\n");
        } else {
            printf("File opened successfully\n");
            close(fd);
        }
    }

    // Attempt to open a file with insufficient permissions
    fd = open("restricted.txt", O_RDONLY);
    if (fd == -1) {
        // Check error if permissions are denied
        if (errno == EACCES) {
            printf("Error: Permission denied.\n");
        } else {
            printf("File opened successfully\n");
            close(fd);
        }
    }

    return 0;
}

/*
Explanation
The program demonstrates how to handle errors from system calls in C

It attempts to open two files, checks the return value of the open call, and prints corresponding error messages using errno and strerror to handle 'file not found' and 'permission denied' errors.
*/