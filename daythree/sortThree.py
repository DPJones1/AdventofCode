import os
import re

def read_csv():
    file_path = "C:/Users/DPJon/OneDrive/Documents/Dev/AdventofCode/daythree/datathree.csv"
    # Specify the relative path to the file
    # Debugging help: Show the absolute path being used
    print(f"Looking for file at: {os.path.abspath(file_path)}")
    
    # Open the file and read its content
    with open(file_path, 'r') as file:
        return file.read()  
    # Read the entire file as a single string

def process_csv():
    # Read the content of the file using the `read_csv` function
    data = read_csv()

    # Regular expressions to match patterns in the data
    mul_pattern = re.compile(r"mul\(([-+]?[0-9]*\.?[0-9]+),\s*([-+]?[0-9]*\.?[0-9]+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    # Initialize variables for the total sum, valid rows, and enabled flag
    total = 0
    valid_rows = []
    mul_enabled = True  # Start with mul instructions enabled

    # Process each character in the data
    index = 0
    while index < len(data):
        # Check for mul(x, y) instructions
        mul_match = mul_pattern.match(data, index)
        if mul_match:
            x, y = map(float, mul_match.groups())
            if mul_enabled:
                result = x * y
                total += result
                valid_rows.append((x, y, result))
            index = mul_match.end()
            continue

        # Check for do() instruction
        do_match = do_pattern.match(data, index)
        if do_match:
            mul_enabled = True  # Enable mul instructions
            index = do_match.end()
            continue

        # Check for don't() instruction
        dont_match = dont_pattern.match(data, index)
        if dont_match:
            mul_enabled = False  # Disable mul instructions
            index = dont_match.end()
            continue

        # Move to the next character if no match was found
        index += 1

    return total, valid_rows

# Example usage
if __name__ == "__main__":
    # Process the file and calculate results
    total, valid_rows = process_csv()

    # Print the total sum of all valid multiplications
    print(f"Total of all valid multiplications: {total}")
