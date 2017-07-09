"""Example of creating files using python."""

filename = "test-write.txt"
fobj = open(filename, "w")
fobj.write("Apples\n")
fobj.write("Bananas\n")
fobj.close()

shoppingList = ["Carrots", "Pears", "Oranges"]
fobj = open(filename, "w")
for item in shoppingList:
    fobj.write(item + "\n")

fobj.close()
