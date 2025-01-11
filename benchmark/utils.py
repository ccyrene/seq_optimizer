def generate_expect_output(length=1e6):
    
    data = list(range(0, int(length)))
    
    return data

def generate_input_data(length=1e6, sub_list_count=10000, overlapping=3):
    """
    Generate input data as a list of sub-lists with defined overlaps.
    Each sub-list is created such that the full range [0, length) is covered.

    Parameters:
        length (int): Total length of the sequence.
        sub_list_count (int): Number of sub-lists to generate.
        overlapping (int): Number of overlapping elements between consecutive sub-lists.

    Returns:
        List[List[int]]: A list of overlapping sub-lists covering the full range.
    """
    # Total number of elements to generate
    total_length = int(length)
    sub_list_count = int(sub_list_count)
    
    # Calculate the step size for sub-lists
    # Ensure step size accounts for overlapping regions
    step = (total_length - overlapping) // (sub_list_count - 1)
    
    input_data = []
    for i in range(sub_list_count):
        start = i * step
        end = start + step + overlapping
        if end > total_length:
            end = total_length
        input_data.append(list(range(start, end)))
    
    return input_data