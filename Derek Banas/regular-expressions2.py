import re
 
# Did you find a match
# if re.search("REGEX", yourString)
 
# Get list of matches
# print("Matches :", len(re.findall("REGEX", yourString)))
 
# Get a pattern object
# regex = re.compile("REGEX")
 
# Substitute the match
# yourString = regex.sub("substitution", yourString)
 
# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length
 
# ---------- Matching Zero or One ----------
 
randStr = "cat cats"
 
regex = re.compile("[cat]+s?")
 
matches = re.findall(regex, randStr)
 
# Match cat or cats
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# ---------- Matching Zero or More ----------
# * matches zero or more of what proceeds it
 
randStr = "doctor doctors doctor's"
 
# Match doctor doctors or doctor's
regex = re.compile("[doctor]+['s]*")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
# You can do the same by setting an interval match
regex = re.compile("[doctor]+['s]{0,2}")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)

    # ---------- Greedy & Lazy Matching ----------
 
randStr = "<name>Life On Mars</name><name>Freaks and Geeks</name>"
 
# Let's try to grab everything between <name> tags
# Because * is greedy (It grabs the biggest match possible)
# we can't get what we want, which is each individual tag
# match
regex = re.compile(r"<name>.*</name>")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# We want to grab the smallest match we use *?, +?, or
# {n,}? instead
 
regex = re.compile(r"<name>.*?</name>")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# ---------- Word Boundaries ----------
# We use word boundaries to define where our matches start
# and end
 
# \b matches the start or end of a word
 
# If we want ape it will match ape and the beginning of apex
randStr = "ape at the apex"
 
regex = re.compile(r"ape")
 
# If we use the word boundary
regex = re.compile(r"\bape\b")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# ---------- String Boundaries ----------
# ^ : Matches the beginning of a string if outside of
#     a [ ]
# $ : Matches the end of a string
 
# Grab everything from the start of the string to @
randStr = "Match everything up to @"
 
regex = re.compile(r"^.*[^@]")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# Grab everything from @ to the end of the line
randStr = "@ Get this string"
 
regex = re.compile(r"[^@\s].*$")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# Grab the 1st word of each line using the the multiline
# code which allows for the targeting of each line after
# a line break with ^
randStr = '''Ape is big
Turtle is slow
Cheetah is fast'''
 
regex = re.compile(r"(?m)^.*?\s")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)
 
# ---------- Subexpressions ----------
# Subexpressions are parts of a larger expression
# If you want to match for a large block, but
# only want to return part of it. To do that
# surround what you want with ( )
 
# Get just the number minus the area code
randStr = "My number is 412-555-1212"
 
regex = re.compile(r"412-(.*)")
 
matches = re.findall(regex, randStr)
 
print("Matches :", len(matches))
 
for i in matches:
    print(i)