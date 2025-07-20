# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Score: 10

# Read input values
s, t = map(int, input().split())  # House start and end point
a, b = map(int, input().split())  # Apple tree and orange tree position
m, n = map(int, input().split())  # Number of apples and oranges

# Distances apples fell from the apple tree
apples = list(map(int, input().split()))

# Distances oranges fell from the orange tree
oranges = list(map(int, input().split()))

# Count how many apples fell on the house
apple_count = 0
for d in apples:
    if s <= a + d <= t:  # Final position of apple is within house range
        apple_count += 1

# Count how many oranges fell on the house
orange_count = 0
for d in oranges:
    if s <= b + d <= t:  # Final position of orange is within house range
        orange_count += 1

# Print the results
print(apple_count)
print(orange_count)
