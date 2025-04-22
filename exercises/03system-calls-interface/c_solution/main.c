#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

/*
    Explanation
        The code snippet demonstrates process creation and management using C system calls

        It creates a child process using fork()

        The child process then uses exec() to run a new program ('ls' command in this case)

        The parent process waits for the child to finish using wait(), ensuring synchronization between processes.
*/ 


int main() {
    pid_t pid = fork();
    if (pid < 0) {
        // Fork failed
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process
        execlp("/bin/ls", "ls", NULL);
        // Only returns if execlp fails
        perror("execlp failed");
    } else {
        // Parent process
        wait(NULL); // Wait for the child process to finish
        printf("Child process finished\n");
    }
    // Both processes will reach this point
    // printf("This is a message from both processes.\n");
    return 0;
}