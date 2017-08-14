"""Example of reading or opening files using python."""

filename = "date-and-time.py"

with open(filename) as fobj:
    content = fobj.readlines()

print(content)

for line in content:
    print(line)

for line in content:
    print(line),  # the use of a commar removes the spaces on each line
