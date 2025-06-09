// Write a C program that demonstrates the use of the 'fork()' system call to create a new process, 
// and uses 'getpid()' and 'getppid()' to print the process IDs of both the parent and child processes.
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork(); // Create a new process
    if (pid < 0) {
        // check if fork() failed
        perror("Fork failed");
        return 1;
    }

    if (pid == 0) {
        // This block is excuted by the child process
        printf("Child Process: PID=%d, Parent PID=%d\n", getpid(), getppid());
    } else {
        // This block is executed by the parent process
        printf("Parent Process: PID=%d, Child PID=%d\n", getpid(), pid);
    }

    return 0;
}

/*
Explanation
The code demonstrates process creation using the 'fork()' system call

After calling 'fork()', the program checks whether the call was successful and whether it is running in the parent or child process

It then prints the process ID of the parent or child process using 'getpid()' and 'getppid()', helping to show concurrent execution.
*/