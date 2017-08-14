"""Example of an array or 'list'."""

grocerties = ["Apples", "Bananas", "Pears"]
print(grocerties)
print(grocerties[0])  # prints first element in array

grocerties.append("Meat")  # adds new element to array
grocerties.remove("Bananas")  # removes Bananas from array
print(grocerties)

people = ["James", "Charmian", "Jimmy", "Linda"]
people.sort()  # sort alphabetically
people.reverse()  # sorts from last to first item in array
print(people)
