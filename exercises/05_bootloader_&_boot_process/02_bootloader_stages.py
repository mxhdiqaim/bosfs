"""
Explanation
This code simulates a simple bootloader process with three stages

Each stage is represented by a function that prints a message indicating its task and then proceeds to call the next stage function

This reflects how a bootloader sequentially initializes and loads each required stage to eventually boot the OS
"""

def stage1():
    print("Stage 1: Initializing hardware and setting up the environment.")
    stage1_5()

def stage1_5():
    print("Stage 1.5: Performing additional hardware checks and configurations.")
    stage2()

def stage2():
    print("Stage 2: Loading the bootloader into memory.")

stage1()
