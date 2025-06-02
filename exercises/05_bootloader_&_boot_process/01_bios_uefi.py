"""
Explanation
This function simulates a simple boot process

It checks the hardware status, initializes hardware, loads a bootloader based on a mock BIOS/UEFI check, and then simulates starting the OS

It demonstrates conditional logic in boot sequences and simulates decision points.
"""

def boot_process(hardware_status):
    if hardware_status == "ok":
        print("Hardware initiated.")

        bootloader = "GRUB" if is_uefi() else "MBR"

        print(f"Bootloader: {bootloader} is loaded.")

        print("OS is booting...")
    else:
        print("Hardware failure detected. Boot process halted.")
    


def is_uefi():
    # Mock func to randomly decide BIOS/UEFI
    return True  # Change to False to simulate BIOS

# Example usage
boot_process("ok")
boot_process("fail")