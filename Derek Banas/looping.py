# Every program has the ability to perform actions on a list of
# values. The for loop can be used to do this.
 
# Each time we go through the loop variable i's value will be
# assigned the next value in our list
 
for i in [2,4,6,8,10]:
    print("i = ", i)
 
# We can also have range define our list for us. range(10) will
# create a list starting at 0 and go up to but not include
# the value passed to it.
 
for i in range(10):
    print("i = ", i)
 
# We can define the starting and ending value for range
for i in range(2, 10):
    print("i = ", i)
 
# You can use modulus to see if a number is odd or even
# If we divide an even by 2 there will be no remainder
# so if i % 2 == 0 we know it is true
i = 2
print((i % 2) == 0)
 
# ---------- PROBLEM : PRINT ODDS FROM 1 to 20 ----------
# Use a for loop, range, if and modulus to print out the odds
 
# Use for to loop through the list from 1 to 21
 
for i in range(1, 21):
 
# Use modulus to check that the result is NOT EQUAL to 0
# Print the odds
 
    if ((i % 2) != 0):
        print("i = ", i)
 
# ---------- WORKING WITH FLOATS ----------
# Floating point numbers are numbers with decimal values
 
your_float = input("Enter a float: ")
 
# We can convert a string into a float like this
 
your_float = float(your_float)
 
# We can define how many decimals are printed being 2
# here by putting :.2 before f
print("Rounded to 2 decimals : {:.2f}".format(your_float))
 
# ---------- PROBLEM : COMPOUNDING INTEREST ----------
# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment +
# their investment * the interest rate
# Print out their earnings after a 10 year period
 
# Ask for money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")
 
# Convert value to a float
money = float(money)
 
# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
 
# Cycle through 10 years using for and range from 0 to 9
for i in range(10):
 
    # Add the current money in the account + interest earned that year
    money = money + (money * interest_rate)
 
# Output the results
print("Investment after 10 years: {:.2f}".format(money))
 
# ---------- WORKING WITH FLOATS ----------
# When working with floats understand that they are not precise
 
# This should print 0 but it doesn't
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)
 
# Floats will print nonsense beyond 16 digits of precision
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001
 
print("Answer : {:.32}".format(i + j))
 
# ---------- ORDER OF OPERATIONS ----------
# When making calculations unless you use parentheses * and /
# will supersede + and -
 
print("3 + 4 * 5 = {}".format(3 + 4 * 5))
 
print("(3 + 4) * 5 = {}".format((3 + 4) * 5))
 
# ---------- THE WHILE LOOP ----------
# We can also continue looping as long as a condition is true
# with a while loop
 
# While loops are used when you don't know how many times
# you will have to loop
 
# We can use the random module to generate random numbers
import random
 
# Generate a random integer between 1 and 50
rand_num = random.randrange(1, 51)
 
# The value we increment in the while loop is defined before the loop
i = 1
 
# Define the condition that while true we will continue looping
while (i != rand_num):
 
    # You must increment your iterator inside the while loop
    i += 1
 
# Outside of the while loop when we stop adding whitespace
print("The random value is : ", rand_num)
 
# ---------- BREAK AND CONTINUE ----------
# Continue stops executing the code that remains in the loop and
# jumps back to the top
 
# Break jumps completely out of the loop
 
i = 1
 
while i <= 20:
 
    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue
 
    # If i equals 15 stop looping
    if i == 15:
        break
 
    # Print the odds
    print("Odd : ", i)
 
    # Increment i
    i += 1