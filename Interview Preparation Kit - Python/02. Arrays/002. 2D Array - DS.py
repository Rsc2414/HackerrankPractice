# Problem: https://www.hackerrank.com/challenges/2d-array/problem
# Score: 15
# Created by: @Rsc2414

# Function to calculate the hourglass sum starting at position (i, j)
def hourglass_sum(arr, i, j):
    top = sum(arr[i][j:j+3])                # Top row of hourglass
    middle = arr[i+1][j+1]                  # Middle of hourglass
    bottom = sum(arr[i+2][j:j+3])           # Bottom row of hourglass
    return top + middle + bottom

# Read 6x6 2D array input
arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))

# Initialize max sum with the first hourglass (top-left corner)
max_sum = hourglass_sum(arr, 0, 0)

# Loop through all valid hourglass starting points
for i in range(4):             # Only go up to row 3 (index 0 to 3)
    for j in range(4):         # Only go up to column 3 (index 0 to 3)
        current_sum = hourglass_sum(arr, i, j)
        max_sum = max(max_sum, current_sum)

# Print the maximum hourglass sum
print(max_sum)
