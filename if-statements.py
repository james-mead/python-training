"""Example of an if statement."""

age = 17
if age < 18:
    print("Sorry, not allowed")
else:
    print("OK, allowed")

luckyNumber = 8  # define variable
if luckyNumber == 7:
    print("Winner!")

if luckyNumber != 7:  # using NOT operator
    print("Try again")

if age == 17 and luckyNumber == 8:  # using an AND operator
    print("Wow, both conditions are true")
