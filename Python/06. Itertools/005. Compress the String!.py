from itertools import groupby

# Take input string
s = input()

# Initialize an empty list to store the result
result = []

# Group the string using groupby
for digit, group in groupby(s):
    count = len(list(group))  # Count how many times the digit repeats
    result.append((count, int(digit)))  # Add tuple to result list

# Print the result, unpacked
print(*result)

