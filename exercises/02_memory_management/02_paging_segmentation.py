def handle_page_segmentation(page_table, page_number, free_frames):
    # Check if a free frame is available
    if not free_frames:
        raise MemoryError('No free frames available for handling the page fault.')
    
    # Simulate loading the page from disk by assigning it a frame
    frame_number = free_frames.pop(0)  # Get the first free frame
    page_table[page_number] = frame_number  # Map the page to the frame
    print(f'Loaded page {page_number} into frame {frame_number}.')
    # return page_table, free_frames

# Example usage
page_table = {}
free_frames = [0, 1, 2, 3]  # List of free frames
page_number = 5  # Page number to handle

handle_page_segmentation(page_table, page_number, free_frames) # Simulate a page fault for page 5