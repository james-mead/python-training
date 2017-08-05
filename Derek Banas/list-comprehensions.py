# ---------- LIST COMPREHENSIONS ----------
# A list comprehension executes an expression against an iterable
 
# Note: While they are super powerful, try not to make list
# comprehensions that are hard to figure out for others
 
# To multiply 2 times every value with a map we'd do
print(list(map((lambda x: x * 2), range(1, 11))))
 
# With a list comprehension we'd do
# Note that a list comprehension is surrounded by []
# because it returns a list
print([2 * x for x in range(1, 11)])
 
# To construct a list of odds using filter we'd
print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
 
# To do the same with a list comprehension
print([x for x in range(1, 11) if x % 2 != 0])
 
# A list comprehension can act as map and filter
# on one line
# Generate a list of 50 values and take them to the power
# of 2 and return all that are multiples of 8
 
print([i ** 2 for i in range(50) if i % 8 == 0])
 
# You can have multiple for loops as well
# Multiply all values in one list times all values in
# another
print([x * y for x in range(1, 3) for y in range(11, 16)])
 
# You can put list comprehensions in list comprehensions
# Generate a list of 10 values, multiply them by 2 and
# return multiples of 8
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])