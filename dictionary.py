"""Example of a dictionary."""

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
print(words)
print(words["Hello"])  # outputs the VALUE of the key

collection = {}
collection[0] = 123
collection[1] = 254
collection[2] = 234
print(collection)
del(collection[0])  # deletes first key/value pair from collection
print(collection)
