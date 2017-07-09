"""Example of creating csv files using python."""

fobj = open("test.csv", "w")
fobj.write("firstName, lastName, salary,\n")
employees = [("James", "Mead", 100000), ("Charmian", "Mead", 900000)]
for employee in employees:
    first = employee[0]
    last = employee[1]
    money = str(employee[2])
    fobj.write(first + "," + last + ',' + money + ",\n")
fobj.close()
