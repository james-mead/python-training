# ---------- MAP ----------
# Map allows us to execute a function on each item in a list
 
# Generate a list from 1 to 10
oneTo10 = range(1, 11)
 
# The function to pass into map
def dbl_num(num):
    return num * 2
 
# Pass in the function and the list to generate a new list
print(list(map(dbl_num, oneTo10)))
 
# You could do the same thing with a lambda
print(list(map((lambda x: x * 3), oneTo10)))
 
# You can perform calculations against multiple lists
aList = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(aList)
 
# ---------- FILTER ----------
# Filter selects items from a list based on a function
 
# Print out the even values from a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))