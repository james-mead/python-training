# convert miles to kilometers
# kilometers = miles * 1.60934

# kilometer variable
kilometer = 1.60934

# Ask the use to enter miles to convert
miles = input("Enter miles ")

# Convert string to integer
miles = int(miles)

# Perform calculation to get value of kilometers
kilometers = miles * kilometer

# Print output to screen
print("{} miles is equal to {} kilometers".format(miles, kilometers))
