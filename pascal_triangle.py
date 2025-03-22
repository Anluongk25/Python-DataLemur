def generate_pascals_triangle(numRows):
    result = [[1]]  # Start with the first row
    
    for i in range(1, numRows):
        prev_row = result[-1]  # Get the previous row
        new_row = [1]  # First element is always 1
        
        # Generate the middle values
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # Last element is always 1
        result.append(new_row)  # Add the new row to the result
    
    return result