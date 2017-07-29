'''
If age is 5, go to kindergarten
Ages 6 through to 17 goes to grades 1 through 12
If age is greater than 17, go to college
'''

#!/usr/bin/python3
# Ask user to input age
age = input("What is your age? ")

# Convert string to Integer)
age = int(age)

if age == 5:
    print("You are at Kindergarten")

# If age is 6 through to 17
elif (age > 5) and (age < 18):
    grade = age - 5
    print("Go to {}th grade".format(grade))

# Handle everyone else
else:
    print("Go to College")