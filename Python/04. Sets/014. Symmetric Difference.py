# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

# Symmetric difference
sym_diff = a.symmetric_difference(b)

# Print each element in sorted order
for num in sorted(sym_diff):
    print(num)
