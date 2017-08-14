#!/usr/bin/python3
# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning
 
norm_string = input("Enter a string to hide in uppercase: ")
 
secret_string = ''
# Cycle through each character in the string
for i in norm_string:
    
    # Store each character code in a new string
    # To accommodate 2 and 3 letter unicode numbers, we subtract 23 and then add 23 when converting back. 
    secret_string += str(ord(i) - 23)
 
print("Secret Message: ", secret_string)

norm_string = ''
# Cycle through each character code 2 at a time by incrementing by
# 2 each time through since unicodes go from 65 to 90
for i in range(0, len(secret_string)-1, 2):
 
    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]
    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code) + 23)

print("Original Message :", norm_string)
 