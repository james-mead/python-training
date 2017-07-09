"""Example of a tuple."""

tuple1 = (1,)  # singular item in tuple must include a commar at the end
tuple2 = ("James", "Charmian", 31)  # tuples cannot be modified dynamically
tuple2 = tuple2 + (38,)

print(tuple2)  # print entire tuple
print(tuple2[0])  # prints first element in tuple
print(tuple2[0][0])  # prints first element and first item

list = list(tuple2)  # converts tuple to a list for modification
list[0] = "Jimmy"  # modified first element in list

print(list)

tuple3 = tuple(list)  # converts list to a tuple

print(tuple3)
