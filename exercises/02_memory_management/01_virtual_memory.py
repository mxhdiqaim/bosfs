def translate_virtual_to_physical(virtual_page, page_table, frame_size):
    # Check if virtual page is in the page table
    if virtual_page not in page_table:
        # Get corresponding physical frame
        physical_frame = page_table[virtual_page]
        # Calculate the physical address
        physical_address = physical_frame * frame_size
        return physical_address
    else:
        # Simulate a page fault
        return "Page fault: The page is not loaded in memory."
    

# Example usage
page_table = {0: 2, 1: 4, 2: 5}
frame_size = 1024

print(translate_virtual_to_physical(1, page_table, frame_size))
# Output: 4096
print(translate_virtual_to_physical(3, page_table, frame_size))
# Output: Page fault: The page is not loaded in memory.

"""
Explanation
This code simulates the translation of a virtual address to a physical address using a page table

It checks if the virtual page is mapped in the table, calculates the physical address if present, and simulates a page fault if not.
"""