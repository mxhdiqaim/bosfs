// Required for malloc and free
#include <stdlib.h>
// Required for printf
#include <stdio.h>

void allocate_memory(int size) {
    // Request allocation of memory
    int *ptr = (int *)malloc(size * sizeof(int));
    if (ptr == NULL) {
        // Error handling if memory allocation fails
        printf("memory allocation failed\n");

        return;
    }

    // Perform operations on allocated memory
    printf("memory allocation successful\n");
    
    // For demonstration, we'll free memory immediately
    free(ptr);
    printf("memory freed\n");
}


int main() {
    int size = 10;
    // Call function with size 10
    allocate_memory(size);
    printf("Exiting program\n");
    return 0;
}