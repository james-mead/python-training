#!/usr/bin/python3
# 1. Decrement spaces by 1 each time in the loop
# 2. Increment the hashes by 2 each time in the loop
# 3. Save space to the stump by calculating tree height -1
# 4. Decrement tree height until it equals 0
# 5. Print spaces and hashes for each row
# 6. Print stump spaces and then 1 hash 

# Get the number of rows for the tree
tree_height = input('How tall is your tree? ')

# Convert string to an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start before incremented
hashes = 1

# Save stump spaces till later
stump_spaces = spaces

# Make sure the right number of rows are printed
while (tree_height != 0):
    

# Print the spaces
# end="" ensures that a new line is NOT created
    for i in range(spaces):
        print(' ', end="")

# Print the hashes
    for i in range(hashes):
        print('#', end="")

# Newline after each row is printed
    print()

# Spaces are decremented by 1 each time
    spaces -= 1

# Hashes are incremented by 2 each time
    hashes += 2

# Decrement tree height each time to jump out of the loop
    tree_height -= 1

# Print the spaces before the stump and finally the stump hash
for i in range(stump_spaces):
    print(' ', end="")

print ('#')