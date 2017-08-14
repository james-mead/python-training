# ---------- ITERABLES ----------
# An iterable is a stored sequence of values (list) or,
# as we will see when we cover generators, an
# object that produces one value at a time
 
# Iterables differ from iterators in that an iterable
# is an object with an __iter__ method which returns
# an iterator. An iterator is an object with a
# __next__ method which retrieves the next value from
# sequence of values
 
# Define a string and convert it into an iterator
sampStr = iter("Sample")
 
print("Char :", next(sampStr))
print("Char :", next(sampStr))
 
# You can add iterator behavior to your classes
class Alphabet:
 
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]
 
alpha = Alphabet()
 
for letter in alpha:
    print(letter)
 
# Iterate through a dictionary because it is an iterable
derek = {"fName": "Derek", "lName": "Banas"}
 
for key in derek:
    print(key, derek[key])