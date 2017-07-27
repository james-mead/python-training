# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''
 
# Ask for a string
orig_string = input('Convert to acronym: ')
 
# Convert the string to all uppercase

orig_string = orig_string.upper()
 
# Convert the string into a list
words = orig_string.split() 
 
# Cycle through the list
for word in words:
 
    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")

print()
 