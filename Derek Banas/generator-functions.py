# ---------- GENERATOR FUNCTIONS ----------
# A generator function returns a result generator when called
# They can be suspended and resumed during execution of
# your program to create results over time rather then
# all at once
 
# We use generators when we want to big result set, but
# we don't want to slow down the program by creating
# it all at one time
 
# Create a generator that calculates primes and returns
# the next prime on command
 
def isprime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):
 
        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    return True
 
# This is the generator
def gen_primes(max_number):
 
    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):
 
        if isprime(num1):
 
            # yield is what makes this a generator
            # When called by next it will return the
            # next result
            yield num1
 
# Create a reference to the generator
prime = gen_primes(50)
 
# Call next for each result
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))