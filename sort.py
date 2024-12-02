# Read the file
with open('data.csv', 'r') as file:
    column1, column2 = [], []
    
    # Skip the header row
    next(file)
    
    for line in file:
        # Split the line by spaces or commas
        numbers = line.strip().replace(",", " ").split()
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

# Sort the columns
column1.sort()
column2.sort()

# Calculate the absolute differences
differences = [abs(a - b) for a, b in zip(column1, column2)]


sum_of_differences = sum(differences)
print("Sum of differences: ", sum_of_differences)

# Save results to a file
with open('results.csv', 'w') as outfile:
    outfile.write('Column1,Column2,Difference\n')
    for c1, c2, diff in zip(column1, column2, differences):
        outfile.write(f"{c1},{c2},{diff}\n")
