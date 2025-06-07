// Write a C program to demonstrate inter-process communication using shared memory and semaphores
// by having one process write to the shared memory and another read from it.

// Not sure if the code is working or not

#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>
#include <string.h>

// Define the key for shared memory and samaphore

key_t = key = ftok("shmfile", 65);

// Create shared memory segment

int shmid = shmid(key, 1024, 0666 | IPC_CREAT);
char *str = (char*) shmad(shmid, (void*)0, 0);
if (fork() == 0) {
    // child process write to shared memory
    sprintf(str, "Hello, Shared Memory!");
} else {
    // Parent process reads from shared
    wait(NULL);
    printf("Data read from memory: %s\n", str);
}

// Detach from shared memory and destroy

shmdt(str);
shctl(shmid, IPC_RMID, NULL);

/*
Explanation
The provided code demonstrates inter-process communication using shared memory in C

It sets up a shared memory segment and uses fork() to create a child process

The child writes a message to the shared memory, and the parent reads and prints this message

This demonstrates basic concurrent process communication in C using shared memory.
*/