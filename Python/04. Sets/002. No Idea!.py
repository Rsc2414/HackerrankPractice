#By @Rsc2414
# Read the input but ignore the first line (not needed here)
_ = input()

# Read the array of elements
elements = input().split()

# Read the set of elements you like
liked_elements = set(input().split())

# Read the set of elements you dislike
disliked_elements = set(input().split())

# Initialize happiness score
happiness = 0

# Go through each element in the array
for item in elements:
    if item in liked_elements:
        happiness += 1  # Add 1 if it's in the liked set
    elif item in disliked_elements:
        happiness -= 1  # Subtract 1 if it's in the disliked set

# Print the final happiness score
print(happiness)
