# Problem: https://www.hackerrank.com/challenges/pairs/problem
# Score: 50

# Read input: n = number of elements, value = target difference
n, value = map(int, input().split())

# Read and sort the array
points = sorted(map(int, input().split()))

# Initialize two pointers
i = 0  # First pointer
j = 1  # Second pointer
ans = 0  # Count of valid pairs

# Loop through the array
while j < n:
    diff = points[j] - points[i]  # Calculate difference

    if diff == value:
        # Found a valid pair
        ans += 1
        j += 1  # Move j to check next pair
    elif diff < value:
        # Difference too small, move j forward
        j += 1
    else:
        # Difference too large, move i forward
        i += 1

    # Ensure i is always less than j
    if i == j:
        j += 1

# Output the answer
print(ans)
