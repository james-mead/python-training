# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest
# Print out the earnings after a ten year period

# Ask the user for investment amount and interest rate
investment = input("How much do you wish to invest? ")
interest_rate = input("What is the current interest rate? ")

# Convert the value to a floating point number
investment = float(investment)

# Conver the value to a floating point number and round to 2 decimal places
interest_rate = float(interest_rate)

# Cycle through each year from year 0 to 9
sum = 0
for i in range(10):
    sum = investment + (investment * interest_rate)

# Output the results
print('Investment after 10 years is equal to {:.2f}'.format(sum))
