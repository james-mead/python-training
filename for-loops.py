"""Example of for loops."""

# simple loop for a range of values
for i in range(0, 10):
    print("Looping", i)

list1 = [1, 2, 3, 4, 5]
# looping through each element in a list
for list in list1:
    print('Looping', list)

# Prints out 3,5,7. The xRange is the iterator, in this example 2
for x in range(3, 8, 2):
    print(x)

"""Example of a while loop."""
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print("counting", count)
    count += 1  # This is the same as count = count + 1

'''
break is used to exit a for loop or a while loop,
whereas continue is used to skip the current block,
and return to the "for" or "while" statement.
'''

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
