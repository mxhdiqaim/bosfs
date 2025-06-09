// Create a basic Linux kernel module that sets up a custom system call and demonstrate a user-space application invoking it.
#include <linux/kernel.h>
#include <linux/syscalls.h>
#include <linux/uaccess.h>

SYSCALL_DEFINE1(my_syscall, char, __user *, user_input) {
    char kernel_buff[256];
    // Copy data from user space to kernel space
    if (copy_from_user(kernel_buff, user_input, 256))  {
        printk(KERN_ERR "Error copying data from user space\n");
        return -EFAULT; // Return error if copy fails
    }

    printk(KERN_INFO "Message from user: %s\n", kernel_buff);

    return 0; // Return success
}

/*
Explanation
This kernel module defines a custom system call 'my_syscall' using C

It copies a string input from the user space to kernel space and outputs it to the kernel log

The 'SYSCALL_DEFINE1' macro is used to define a system call with one parameter.
*/