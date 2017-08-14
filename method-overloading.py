"""Example of a method."""

def collect(a, b=None):  # =None states that the parameter is optional
    if b is None:
        return a
    else:
        return a + b


print(collect(1))
print(collect(1, 2))
