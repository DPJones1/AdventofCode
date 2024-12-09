import os

def read_csv():
    reports = []
    # This will store all of the reports to make it easier to parse

    print(f"Looking for file at: {os.path.abspath('daytwo/dataTwo.csv')}")  # Debugging help
    with open('daytwo/dataTwo.csv', 'r') as file:
        # Opens the file to read it
        for line in file:
            # Iterate through each line in the file
            levels = list(map(int, line.strip().split()))
            # Splits the line by spaces, converts each value from string to int
            reports.append(levels)
            # Adds the processed line (report) to the list
    return reports

def is_monotonic(levels):
    # Checks if the values in the report are strictly increasing or strictly decreasing
    return all(x < y for x, y in zip(levels, levels[1:])) or all(x > y for x, y in zip(levels, levels[1:]))

def is_difference_valid(levels):
    # Ensures the difference between any two adjacent values in the report is within the range 1 to 3
    # zip(levels, levels[1:]) pairs each value with the next one
    # abs(x - y) calculates the absolute difference between adjacent values
    # 1 <= ... <= 3 ensures the difference is between 1 and 3
    # all(...) confirms that this holds for the entire report
    return all(1 <= abs(x - y) <= 3 for x, y in zip(levels, levels[1:]))

def is_safe(levels):
    # A report is "safe" if it is both monotonic and has valid differences
    return is_monotonic(levels) and is_difference_valid(levels)

def is_safe_with_one_removal(levels):
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports():
    # Reads all reports from the file and counts how many are safe
    reports = read_csv()  # Ensure this calls the corrected `read_csv()` function
    safe_count = 0 

    for report in reports:
        if is_safe(report):
            safe_count += 1
        #Firt checking if report is safe without any amends to report

        elif is_safe_with_one_removal(report):
            safe_count += 1
    return safe_count
    # if not safe then we look to remove one level to make it so
     
# Main script
safe_reports_count = count_safe_reports()  # Calls the function to count safe reports
print(f"Number of safe reports: {safe_reports_count}")  # Outputs the result
